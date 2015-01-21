import argparse
import os
import sys
import sqlite3
import glob
from util import ParseConfig, create_db

class MediaLibraryCondenser():

	def __init__(self, config_file):
		print "running"


def main():
	parser = argparse.ArgumentParser(
		description = 'Find duplicate media files from a set of directories. ' )
	parser.add_argument('-c', '--config', required=True, help='ini-style config',
			                action='store', dest='config')
	args = parser.parse_args()

	mlc = MediaLibraryCondenser(args.config)

if __name__ == '__main__':
	main()
