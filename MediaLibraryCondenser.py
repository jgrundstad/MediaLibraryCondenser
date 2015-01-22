import argparse
import os
import sys
import sqlite3
import glob
from util import ParseConfig, CreateDB

class MediaLibraryCondenser():

	def __init__(self, config_file):
		print "running"
    CDB = CreateDB(config_file)

def main():
	parser = argparse.ArgumentParser(
		description = 'Find duplicate media files from a set of directories. ' )
	parser.add_argument('-c', '--config', required=True, help='ini-style config',
			                action='store', dest='config')
  parser.add_argument('-d', '--createdb', help='create a new file database',
                      action='store_true', dest='createdb')
	args = parser.parse_args()

	mlc = MediaLibraryCondenser(args.config)

if __name__ == '__main__':
	main()
