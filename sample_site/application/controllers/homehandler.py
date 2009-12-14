from basehandler import BaseHandler

class HomeHandler(BaseHandler):
  def get(self):
    # self.write("Yay, it works!")
    self.render("index.html")