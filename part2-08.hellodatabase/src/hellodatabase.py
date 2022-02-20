#!/usr/bin/env python3
import sys
import sqlite3


def read_database(conn):
	cursor = conn.cursor()
	agents = cursor.execute('SELECT * FROM Agent ORDER BY id;').fetchall()
	return agents



def main(argv):
	name = sys.argv[1]
	conn = sqlite3.connect(name)
	agents = read_database(conn)
	for agent in agents:
		print(agent[0], agent[1])

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s database' % sys.argv[0])
	else:
		main(sys.argv)
