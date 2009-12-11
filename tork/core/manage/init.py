import sys, os, distutils.dir_util

sample_site_directory = "/Users/vnguyen/Dropbox/Projects/Tork/sample_site"  # @@@2 Todo(Van): use /opt/local or some convention

def init(argv):
  """Initialize a Tork project in the current directory if that is possible."""
  # @@@3 ToDo(Van): refactor this, maybe OOP?
  if len(argv) == 0:
    print "Tork:  [Error]:  tork init requires a project name."
    exit()
  if os.path.exists("./" + argv[0]):
    print "Tork:  [Error]:  a project already exists in this directory."
    exit()
  if not sample_site_directory:
    print "Tork:  [Error]:  no sample site directory found.  Please reinstall or contact author."
    
  distutils.dir_util.copy_tree(sample_site_directory, "./" + argv[0])
  if os.path.exists("./" + argv[0]):    
    print "Tork: [Success]:", argv[0], "folder created."
  else:
    print "Tork: [Error]:", "unable to create folder in current directory."
    
def main():
  print "Please don't try to run this script separately."
    
if __name__ == '__main__':
  main()