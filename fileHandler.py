#!/usr/bin/python

dir = "/home/gshanmu/Python_tut"

with open(dir + "/inputfile") as fd:
	fd_input = fd.readlines()

output = open(dir + "/outputfile", 'w')

for line in fd_input:
	print line.strip()
	output.write("Output:" + line.strip() + '\n')

output.close()

