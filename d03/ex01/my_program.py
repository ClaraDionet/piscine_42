#!/usr/bin/python3
# coding : utf8

import sys

if __name__== "__main__":
	sys.path.insert(0, '/local_lib')
	import path
	f= open("local_lib/my_file.txt","w+")
	for i in range(5):
		f.write("This is line %d\r\n" % (i+1))
	f.close() 
	f=open("local_lib/my_file.txt", "r")
	if f.mode == 'r': 
		contents =f.read()
		print(contents)