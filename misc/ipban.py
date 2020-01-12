#!/usr/bin/python
# Autors Svabis fizmats@inbox.lv

import os			# file system
import re			# regular expresions
from subprocess import call	# for calling system comands
from datetime import datetime	# for time stamp in output log file

auth_log = '/var/log/auth.log'	# AUTH log
mail_log = '/var/log/mail.log'	# MAIL log

logfile = '/var/log/ipban.log'	# progas log
banlist = []			# IP ierakstu masivs

def searchIP():
	"Search IP adreses to ban in auth.log"
	lines = [line.rstrip('\n') for line in open(auth_log)]

	for line in lines:
		search_str1 = "Failed password for root from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
		result = re.search(search_str1, line)
		if result:
			banlist.append(result.group(1))

		search_str2 = "Failed password for invalid user \w+ from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
		result = re.search(search_str2, line)
		if result:
			banlist.append(result.group(1))

        lines = [line.rstrip('\n') for line in open(mail_log)]
#        for line in lines:
#                search_str1 = "connect from unknown\[(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\]"
#                result = re.search(search_str1, line)
#                if result:
#                        banlist.append(result.group(1))

def listIP():	# -p gadijums
	"Prints out all located IP"
	templist = set(banlist)
	for ban in templist:
		print ban + " BANNED"

def banIP():	# -b gadijums
	"Create/Flush ipban chain, restore ipban list, search unique IP and log them into ipban.log "
	call(['iptables', '-N', 'ipban'])	# create chain ipban
	call(['iptables', '-F', 'ipban'])	# flush chain ipban
	log_ban =[]

# IPBAN LOG read
	lines = [line.rstrip('\n') for line in open(logfile)]

	for line in lines:
        	search_str = "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
	        result = re.search(search_str, line)
	        if result:
		        log_ban.append(result.group(1))

# create uniqu IP adress list and append to ipban.log
	temp_ban_list = set(banlist) - set(log_ban)
	date = datetime.now().strftime('%Y %b %d %H:%M:%S')

	print "unique"
        for ban in temp_ban_list:
                print "loged " + ban

	with open(logfile, "a") as myfile:
		myfile.write("\tipban palaists " + date + "\n")
	        for ban in temp_ban_list:
        	        myfile.write(ban + "\n")
	myfile.close()

# Read updated ipban.log and insert IP into iptables ipban chain
        lines = [line.rstrip('\n') for line in open(logfile)]

        for line in lines:
                search_str = "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
                result = re.search(search_str, line)
                if result:
			call(['iptables', '-I', 'ipban', '1', '-s', result.group(0), '-j', 'DROP'])

searchIP()
listIP()
banIP()
