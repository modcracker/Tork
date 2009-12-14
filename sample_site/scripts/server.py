#!/usr/bin/python

import sys
sys.dont_write_bytecode = True
sys.path.append("../")
from application.server import main as run

def main():
  run()
  
if __name__ == '__main__':
  main()