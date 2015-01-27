import argparse
import glob
import fnmatch
import os
import sys
import sqlite3
from util import ParseConfig, CreateDB

class MediaLibraryCondenser():

  def __init__(self, config_file, createdb):
    print "parsing config file"
    pc = ParseConfig.ParseConfig(config_file)
    self.config = pc.get_dict()

    if createdb:
      CDB = CreateDB.CreateDB(self.config)

    self.walk_dirs()


  def walk_dirs(self):
    for dir in self.config['search'].split(' '):
      print "Walking " + dir
      for root, dirnames, filenames in os.walk(dir):
        print "root: %s" % root
        for filename in fnmatch.filter(filenames, '*.jpg'):
          print os.path.join(root, filename)
        for filename in fnmatch.filter(filenames, '*.JPG'):
          print os.path.join(root, filename)



def main():
  parser = argparse.ArgumentParser(
    description = 'Find duplicate media files from a set of directories. ' )
  parser.add_argument('-c', '--config', required=True, help='ini-style config',
                      action='store', dest='config')
  parser.add_argument('-d', '--createdb', help='create a new file database',
                      action='store_true', dest='createdb', default=0)
  args = parser.parse_args()

  mlc = MediaLibraryCondenser(args.config, args.createdb)

if __name__ == '__main__':
  main()
