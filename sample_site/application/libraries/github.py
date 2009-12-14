import tornado.escape

class GitHub(object):
  """
    Handles GitHub Post Receive Hook JSON payload.  
    
    # Usage Example (inside a Tornado Handler):
      def post(self):
        payload = new GitHub(self.get_argument("payload"))
        branch = payload.get_branch()
        if branch == "master":
          # do stuff
  """
  
  def __init__(self, payload):
    """Decode json into a python dictionary and save it"""
    self.payload = tornado.escape.json_decode(payload)
    
  def get_branch(self):
    """Returns the branch of the payload"""
    return self.payload['ref'].split("/")[2]
    
  def get_json(self, json=False):
    """Returns json in json format or dict as requested"""
    if json:
      return tornado.escape.json_encode(self.payload)
    else:
      return self.payload