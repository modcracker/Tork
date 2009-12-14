#!/usr/bin/python

import os
from controllers.homehandler import HomeHandler

def get_routes():
  return [
    (r"/", HomeHandler)
  ]
  
def get_settings():
  return dict(
    debug=False,
    template_path=os.path.join(os.path.dirname(__file__), "templates")
    # login_url="",
    # import base64, uuid
    # cookie_secret=base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
  )
  
def main():
  print """Don't run this as script."""
  
if __name__ == '__main__':
  main()