#!/usr/bin/python3

import sys
from antigravity import geohash

def geohashing(latitude, longitude, date, indice_dow):
	date_dow = date + "-" + str(indice_dow)
	return geohash(latitude, longitude, date_dow.encode('ascii'))

if __name__ == '__main__' :
	if len(sys.argv) == 5:
		try:
			geohashing(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3], float(sys.argv[4]))
		except ValueError :
			print("latitude, longitude & indice_dow must be of type float")
	else:
		print("enter correct number of arguments: latitude, longitude, date, indice_dow")