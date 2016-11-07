#!/usr/bin/python


import paramiko
import time
import xmltodict
import re

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.56.103', username = 'root', password = 'gimec1234')

#stdin,stdout,stderr = ssh.exec_command("show version")

inter_shell = ssh.invoke_shell()
output = inter_shell.recv(65535)
#print output

inter_shell.send('cli\n')
output = inter_shell.recv(65535)
#print output

inter_shell.send('edit\n')
output = inter_shell.recv(65535)
#print output

inter_shell.send('show protocols bgp | display xml | no-more\n')
time.sleep(5)
output = inter_shell.recv(65535)
xml_output_list = output.split('\n')
bgpconf = []
match = 'False'

for line in xml_output_list:
	ptrn1 = re.escape('<rpc-reply')
	ptrn2 = re.escape('</rpc-reply')
	if re.search (ptrn1,line):
		bgpconf.append(line)
		match = 1
	elif re.search(ptrn2,line):
		bgpconf.append(line)
		match = 0
	elif match == 1:
		bgpconf.append(line)

bgpconfxml = '\n'.join(bgpconf)

xml_parse = xmltodict.parse(bgpconfxml)

for key in xml_parse['rpc-reply']['configuration']['protocols']['bgp']['group']:
	group_name = key['name']
	group_neigh = key['neighbor']['name']
	print "GroupName:"+ group_name + ", NeighborIP:"+ group_neigh  

