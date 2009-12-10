import sys, os
from optparse import OptionParser
import tork

options_list = [
  [["-i", "--init"], {'dest':"init_flag", "default":False, "help":"Initialize a Tornado Web application with MVC folders"}],
  [["-t", "--test"], {'dest':"test_flag", "default":False, "help":"Run all tests for local application"}]
]
commands_list = ["init", "start", "stop", "restart", "test"]

def run(argv=None):
  """ Runs functions that the user calls via the command line. """
  parser = OptionParser(usage="%s subcommand [options] [args]",
                        version=tork.get_version())
  for option in options_list:
    parser.add_option(*option[0], **option[1])
  
  try:
    options, args = parser.parse_args(argv)
  except Exception, e:
    pass # Ignore OptionError
  
  if len(args) >= 1:
    if args[0] in commands_list:
      print args[0], "called"
    else:
      print "Usage:", parser.usage %(os.path.basename(sys.argv[0]))
      print ""
      print "Type 'tork help' for usage information"
  else:
    print "Usage:", parser.usage %(os.path.basename(sys.argv[0]))
  
  