#!/usr/bin/python

import urllib2

def is_running(test_url):
  """Checks if the a server is up or down by looking for HTTP header errors"""
  if test_url:
    req = urllib2.Request(test_url)
    try:
      urllib2.urlopen(req)
    except (urllib2.HTTPError, urllib2.URLError), e:
      return False, "Server Status: Down"
    else:
      return True, "Server Status: Running"
  else:
    raise Exception, "is_running requires a url argument."
    
def get_stack_trace(address, user, pass, path):
  """Logs into given server and runs tail on nohup to return recent errors"""
  # Obviously not done yet
  pass
    
def main():
  """Test if is_running works"""
  print is_running("http://teddy.higut.com/demo")
  print is_running("http://www.higut.com/demo")
  
if __name__ == '__main__':
  main()
  