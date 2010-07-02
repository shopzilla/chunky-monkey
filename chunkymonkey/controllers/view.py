import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from chunkymonkey.lib.base import BaseController, render

from socket import *
import urllib
from urlparse import urlparse

log = logging.getLogger(__name__)

class ViewController(BaseController):

    def index(self):
    	q = request.params.get('q', None)
    	useragent = request.headers.get('User-Agent', None)
    	c.result = False
    	c.chunkedEncoding = True
    	c.chunks = []
    	c.body = ''
		
    	if q:
			url = urlparse(q)
			
			log.info(url)
			
			sock = socket(AF_INET, SOCK_STREAM)
			sock.connect( (url.hostname, ( url.port if url.port else 80) ) )
			httpRequest = 'GET %s?%s HTTP/1.1\r\nHost: %s\r\nAccept: text/html\r\nUser-Agent: %s\r\n\r\n' % (url.path, url.query, url.hostname, useragent)
			
			log.info('HTTP Request\n' + httpRequest)
			
			# Force it to timeout so we can detect the end of the stream
			sock.settimeout(1)
			sock.send(httpRequest)
			
			# Read all content
			total_data=[]
			while True:
				try:
					data = sock.recv(4096)
				except:
					# Timeout exception
					break
				if not data: break
				total_data.append(data)
			sock.close()

			# Combine all the data
			content = ''.join(total_data)
			
			# Separate headers from body
			headers, sep, body = content.partition('\r\n\r\n')

			c.result = True
			
			if headers.lower().find('content-length:') > -1:
				c.chunkedEncoding = False
				c.body = body
			else:
				# make content an array of ( size1, chunk1, size2, chunk2, ..., sizeN, chunkN )
				content = body.split('\r\n')
			
				# Read chunk sizes and content pairs
				chunks = []
				index = 0	
				while index < len(content):
					value = content[index]
					index = index + 1
					try:
						sizeInt = int(value, 16)
					except:
						# Handle the case where there is a rogue \r\n - we don't find a hex value
						# Append it to the last chunk's content
						lastChunk = chunks[len(chunks)-1]
						lastChunk['conent'] = lastChunk['content'] + value
						continue
					if sizeInt == 0: break
					chunks.append( {'sizeHex' : value, 'size' : sizeInt, 'content' : content[index]} )
					index = index + 1
			
				c.chunks = chunks
			
    	return render('/view.mako')
