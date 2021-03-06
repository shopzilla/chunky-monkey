<html>
<head>
<title>ChunkyMonkey</title>
<link rel="stylesheet" type="text/css" href="/brown/templatemo_style.css" />
<script type="text/javascript">
	function toggle(id) {
		el = document.getElementById(id)
		if (el.style.display == 'none') {
			el.style.display = 'block';
		} else {
			el.style.display = 'none';
		}
	}
</script>
</title>
</head>
<body>
	<div id="templatemo_container"> 

    	<div id="templatmeo_header"> 
        	<div id="templatemo_menu"> 
            </div> 

            <div id="templatemo_logo_area"> 
            	<div id="templatemo_logo">ChunkyMonkey</div> 
            </div> 
            <div class="templatemo_welcome"> 
            	<h1>HTTP Response Visualizer</h1> 
                <p>Enter any URL and click Go! to see the individual HTTP Chunked responses returned from the page</p> 
            </div> 
        </div>
        
		<div id="templatemo_content"> 
        	<div id="templatemo_content_top"> 
            	<div id="templatemo_content_bottom"> 
                	<div id="templaetmo_left"> 
                    	<div class="templatemo_one_col">
							<form>
								<h1><label forid="q">Enter a URL:</label></h1>
								<input id="q" type="text" size="100" name="q" value="${request.params.get('q', 'http://www.bizrate.com/laptop-computers/')}" /></label>
								<input type="submit" value="Go!" />
							</form>
                            <div class="cleaner"></div> 
						</div>
                        <div class="templatemo_h_line"></div>
                    	<div class="templatemo_one_col">
                    		% if c.chunkedEncoding:
								% for i, chunk in enumerate(c.chunks):
									<p>Chunk ${i} - ${chunk['sizeHex']}, ${chunk['size']} bytes <a href="javascript:toggle('chunk_content_${i}');">Raw Content</a></p>
									<p id="chunk_content_${i}" style="display:none">
<textarea cols="120" rows="25">
% try:
${chunk['content'] | h}</textarea>
% except:
Error reading chunk</textarea>
% endtry
									</p>
								% endfor
							% else:
								<p>No chunked encoding found <a href="javascript:toggle('responseBody');">Response Body</a></p>
								<p id="responseBody" style="display:none">
<textarea cols="120" rows="25">
% try:
${c.body | h}</textarea>
% except:
Error reading chunk</textarea>
% endtry

								</p>
							% endif

                            <div class="cleaner"></div> 
                        </div> 
                                              
                    </div><!-- End Of Left--> 
                    <div class="cleaner"></div> 
                </div><!-- End Of Content Bottom--> 
            </div><!-- End Of Content Top--> 
        </div><!-- End Of Content--> 
    	<div id="templatemo_bottom_panel"> 
        	<div id="bottom_top"> 
            </div><!-- End Of bottom_top--> 
        </div><!-- End Of templatemo_bottom_panel--> 
        <div id="templatemo_bottom_bottom"> 
        </div> 
        <div id="templatemo_footer"> 
        <a href="http://wiki.shopzilla.com/index.php?title=ChunkyMonkey" target="_parent">ChunkyMonkey Wiki</a> |
        <a href="http://git.shopzilla.com/cgit/cgit.cgi/tools/chunkymonkey/" target="_parent">ChunkyMonkey Git Repo</a> |
        <a href="http://hudson012.shopzilla.laxhq:8420/hudson/job/chunkymonkey/" target="_parent">ChunkyMonkey Builds</a>
        </div>
        
    </div><!-- End Of Container --> 
</body>
</html>
