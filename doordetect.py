#! /usr/bin/env python3

# FILE: doordetect.py
# AUTHOR: Canyon B
# PURPOSE: Door Detector With logs that upload to alternative server

import gpiozero
import datetime
import subprocess
import sys

def pincheck(pin40):
	pin40 = pin.40

def doorcheck():
	pincheck()
	if pin40 == 1:
		writelog()
		continue
	elif pin40 == 1:
		continue

def loglaunch(doorlog,todayinfo,date,time):
	doorlog = open("doorlog.txt", "a+")
	todayinfo = str(datetime.datetime.now())
	date = (todayinfo[0:9])
	time = (todayinfo[11:19])

def writelog(dooropened):
	logvariables()
	doorlog.write(dooropened)

def logvariables(dooropened,header):
	header = ("LOG START "+(date)+' '+(time))
	dooropened = ("DOOR OPENED: "+(date)+ " "+(time)+"\n")
	return header
	return dooropened

def header(doorlogtext, header, doorlog, count):
	try:
		doorlogtext = doorlog.readlines()
		if header not in doorlogtext:
			remotebackup()
			doorlog.write((header))
		except:
			doorlog.write("DOORLOG HEADER ERROR\n")
			continue
	else:
		continue
	return doorlogtext

def hourgrab(hour):
	hour = (str(datetime.datetime.now())[11:13])

def backitup():
	hourgrab()
	if int(hour) % 2 == 1:
		remotebackup()
	else:
		continue

def remotebackup():
	#!!! NEEDS SSH KEY GEN ON SOURCE DOWNLOADED TO DEST
	## prolly need ip check or static ip
	subprocess.run(["scp", "doorlog.txt", "host@server:PATH"])

### class weekdaywatch:
#	def __init__(self,weekdayALP):
#		weekdaynum = (datetime.datetime.now().weekday())
#		weekdaysdict = { 0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:
#		"Friday",5:"Saturday",6:"Sunday"}
#		weekdayALP = (weekdaysdict[weekdaynum])
#	@property
#	def WD(self):
#		return self._WD

#	@WD.setter
#	def WD2(): 



def main():
	header()
	loglaunch()
	doorcheck()

if __name__ == "__main__":
	main()
