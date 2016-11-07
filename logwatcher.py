#!/usr/bin/python3

import time
import re
from mailer import Mailer,Message

logdir = "/var/log"
dir = "/home/gshanmu/Python_tut"


logfile = open(logdir + "/192.168.56.103_syslog.log", 'r')
logfile.seek(0,2)

while True:
	line = logfile.readline()
	if not line:
		time.sleep(0.1)
		continue
	elif re.search('AdjChg.*Full',line):
		line = line.replace('  ',' ')
		neigh = line.split(' ')[5]
		result = "Ospf Adjacency status change alert for Neighbor: " + neigh + "\n"	
		print (result)	
		message = Message(From="gshanmu@Brocade.com",
          	          	  To="gshanmu@Brocade.com",
                  	  	  Subject="AUTO:Alert:: OSPF Neighbor Status Change in VyOS router")

		message.Html = """
        <head>
                <style>
                pre
                {
                font-family:Calibri;
                font-size:11pt;
                }
                </style>
        </head>
        <body>
        <p><pre>Hi,<br><br>
<b>"""+result+"""
</b><br>Regards,
Ganesan Shanmuganathan
SWN-TAC<br>
       <b> <u>NOTE</u>:</b> This is an automated email<br><br><br><br><br><br><br>
<b><u>DISCLAIMER</u>:</b> You are reminded that the material being shared belongs to Brocade and contains sensitive information. Please ensure that you treat this material as confidential and do not forward or disclose any of the information contained herein to anyone outside Brocade.<br></pre></p>"""

		sender = Mailer('mailhost.brocade.com')
		sender.send(message)	




