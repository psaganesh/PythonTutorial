#!/usr/bin/python

import sys

class Hello():
	testing = "Its me"	
	def __init__(self,name):
		print "Hello there, " + name

me = Hello(sys.argv[1])


print Hello.testing

"""
def main():
	print "Hello there, " + sys.argv[1]

print __name__

if __name__ == '__main__':
	main()
"""
