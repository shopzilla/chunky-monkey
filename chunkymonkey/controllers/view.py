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
    	
    	if q:
			url = urlparse(q)

			sock = socket(AF_INET, SOCK_STREAM)
			sock.connect( (url.hostname, ( url.port if url.port else 80) ) )
			httpRequest = 'GET %s HTTP/1.1\r\nHost: %s\r\nAccept: text/html\r\n\r\n' % (url.path, url.hostname)
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

			# Split the content first at CRLFCRLF (which separates headers from body)
			# Then grab the body and split at CRLF which separates chunk size from chunk content
			# content is an array of ( size1, chunk1, size2, chunk2, ..., sizeN, chunkN )
			content = ''.join(total_data).split('\r\n\r\n')[1].split('\r\n')
			
			# Read chunk sizes and content pairs
			chunks = []
			index = 0	
			while index < len(content):
				sizeHex = content[index]
				sizeInt = int(sizeHex, 16)
				if sizeInt == 0: break
				index = index + 1
				chunks.append( {'sizeHex' : sizeHex, 'size' : sizeInt, 'content' : content[index]} )
				index = index + 1
			
			c.chunks = chunks
    	return render('/view.mako')
