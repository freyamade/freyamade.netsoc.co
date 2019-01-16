#!/usr/bin/env python3
import cgi
from cgitb import enable
# enable()  # Traceback. Comment out in production

import os

# Response Headers
print('Content-Type: text/html')
print()  # End of headers
# Response Body
# Percentages are double commented because of how the '%' formatting works
print("""
<!DOCTYPE html>
<html>
    <head>
        <title>crnlpanic - Techtalks and other stuff maybe</title>
        <meta content="width=device-width, initial-scale=1" name="viewport" />
        <link href="//fonts.googleapis.com/css?family=Lato:100" rel="stylesheet" type="text/css">
        <link href="style.css" type="text/css" rel="stylesheet" />
        <meta property="og:title" content="crnlpanic" />
        <meta property="og:url" content="http://%(http_host)s%(request_uri)s" />
        <meta property="og:image" content="http://netsoc.co/rk/wp-content/uploads/2015/10/generic-og.png" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <meta property="og:site_name" content="crnlpanic.netsoc.co" />
        <meta property="fb:admins" content="1385961037" />
        <meta property="og:description" content="crnbrdrck's Netsoc Homepage - Techtalks and other stuff too maybe" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:site" content="@crnbrdrck" />
        <meta name="twitter:description" content="crnbrdrck's Netsoc Homepage - Techtalks and other stuff too maybe" />
        <meta itemprop="image" content="http://netsoc.co/rk/wp-content/uploads/2015/10/generic-og.png" />
    </head>
    <body>
        <div class="container">
            <div class="content">
                <div class="title">techtalks</div>
                <div class="cards">
                    <a class="card" href="/techtalks/css/" target="_blank">
                        <h2>CSS</h2>
                        <img src="https://raw.githubusercontent.com/crnbrdrck/netsoc-css-talk/master/title.png" alt="css title slide" />
                        <p><em>How to style your own website easily by using CSS other people spend ages making.</em></p>
                    </a>
                    <a class="card" href="/techtalks/languages/" target="_blank">
                        <h2>Ruby / Crystal</h2>
                        <img src="https://raw.githubusercontent.com/crnbrdrck/netsoc-languages-talk/master/title.png" alt="ruby / crystal title slide" />
                        <p><em>Syntactic Sugar / Syntactic Sugar with speed</em></p>
                    </a>
                    <a class="card" href="/techtalks/docker/" target="_blank">
                        <h2>Docker</h2>
                        <img src="https://raw.githubusercontent.com/crnbrdrck/netsoc-docker-talk/master/title.png" alt="docker title slide" />
                        <p><em>Containers with a cute whale mascot</em></p>
                    </a>
                </div>
            </div>
        </div>
    </body>
</html>
""" % ({
    'http_host': os.environ['HTTP_HOST'],
    'request_uri': os.environ['REQUEST_URI']
}))
