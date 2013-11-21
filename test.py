import oauth2 as oauth
import urllib2 as urllib
import json
import sys




# See Assignment 1 instructions or README for how to get these credentials
access_token_key = "223231567-NVL80MAUx0I45So4kP9NYIo8WGSe3WR31eUNZFO5"
access_token_secret = "3xyeIXfKKliwj8xV1Msy8nUQKT8KUphdkzGNun6bqo"

consumer_key = "Li0ICHVrbD4v9fgicyGZAw"
consumer_secret = "MeeOXt80hBexJVVVPrpJWmN9We6nLUnm4B9BVVvXgk"

_debug = 0

oauth_token = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  input = open(sys.argv[1])
  for line in input:
      data = json.loads(line)
      keywords = data      
  for i in range(150):
    x = keywords.keys()[i]
    x = str(x)
    url = "https://api.twitter.com/1.1/search/tweets.json?count=100&q="   
    url = url+x
    #tweet_id = str(keywords[x])
    #url = url + "&max_id=" + tweet_id
    parameters = []
    response = twitterreq(url, "GET", parameters)
    #print response.read()
    for line in response:
      apple = json.loads(line)
      print line
if __name__ == '__main__':
  fetchsamples()


	

 





    
