import argparse
import os
import ParseConfig
import sqlite3
import sys

class MediaLibraryCondenser():

	def __init__(self, config_file):
		self.config_file = config_file
		self.parse_config()
		self.init_db()
		self.create_main_table()
	
	def parse_config(self):
		pc = ParseConfig.ParseConfig(self.config_file)
		pc.print_dict()
		self.config_dict = pc.get()


	def init_db(self):
		if os.path.isfile(self.config_dict['db_name']):
			print >>sys.stderr, self.config_dict['db_name'] + " already exists"
			sys.exit()
		self.db = sqlite3.connect(self.config_dict['db_name'])


	def create_main_table(self):
		cursor = self.db.cursor()
		cursor.execute('''
			CREATE TABLE files(id INTEGER PRIMARY KEY, path TEXT, filename TEXT,
												 extension TEXT)''')
		self.db.commit()


def main():
	parser = argparse.ArgumentParser(
		description='Create the sqlite3 database required for the ' \
				+ 'MediaLibraryCondenser')
	parser.add_argument('-c', '--config', help='config file, contains ' \
			                + 'username and password for db creation',
											action='store', dest='config', required=True)
	args = parser.parse_args()

	mlc = MediaLibraryCondenser(args.config)


if __name__ == '__main__':
	main()
