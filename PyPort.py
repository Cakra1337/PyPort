#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *
import os
import sys


print """
  ██▓███  ▓██   ██▓ ██▓███   ▒█████    ██▀███  ▄▄▄█████▓
▓██░  ██▒▒██   ██▒▓██░  ██▒ ▒██▒  ██▒▓██ ▒  ██▒▓   ██▒  ▓▒
▓██░ ██▓▒ ▒██ ██░ ▓██░ ██▓▒ ▒██░  ██▒ ▓██ ░ ▄█ ▒  ▓██░  ▒░
▒██▄█▓▒ ▒ ░ ▐██▓░ ▒██▄█▓▒  ▒▒██   ██░ ▒██▀▀█▄  ░  ▓██▓  ░
▒██▒ ░  ░ ░ ██▒▓  ▒██▒ ░   ░░ ████▓▒░ ░██▓ ▒██▒   ▒██▒  ░
▒▓▒░ ░  ░  ██▒▒▒  ▒▓▒░ ░  ░░ ▒░▒░▒░   ░ ▒▓ ░▒▓░   ▒ ░░
░▒ ░     ▓██ ░▒░  ░▒░        ░ ▒ ▒░     ░▒ ░ ▒░     ░
░░    [==▒=▒=░░===░░=========░=░=░======░░===░=]
      [--░]░                   ░           [---]
      [--░]░         PyPort v1.0           [---]
      [---]    Simple Python Port Scanner  [---]
      [---]     created by CyberCl0wn      [---]
      [---]    facebook.com/CyberCl0wn     [---]
      [---]                                [---]
      [========================================]

"""


if __name__ == "__main__":
	try:
		target=raw_input("Enter target : ")
		targetIP=gethostbyname(target)

		print "Scanning at ",targetIP

		for i in range(20,1025):
			s = socket(AF_INET,SOCK_STREAM)
			result = s.connect_ex((targetIP, i))

			if(result == 0):
				print "Port %d : open." %(i,)
			s.close()

	except (KeyboardInterrupt):
		print "Cancelled."
		try:
			sys.exit(0)
		except(SystemExit):
			os._exit(0)

