#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
from dkb_robo import DKBRobo
import os
from dotenv import load_dotenv

if sys.version_info > (3, 0):
	import http.cookiejar as cookielib
	import importlib

	importlib.reload(sys)
else:
	import cookielib

	reload(sys)
	sys.setdefaultencoding("utf8")


if __name__ == "__main__":

	# .env-Datei laden
	load_dotenv()

	# Zugriff auf Umgebungsvariablen
	username = os.getenv("USERNAME")
	password = os.getenv("PASSWORD")

	DKB = DKBRobo()

	# Using a Contexthandler (with) makes sure that the connection is closed after use
	with DKBRobo(dkb_user=username, dkb_password=password) as dkb:
		print('Last login: ', dkb.last_login)

		document_dictionary = dkb.scan_postbox(
			'/Users/christoph/Meine Ablage (mail@christoph-dietrich.de)/Inbox/DKB/_Automation/', # path
			False, # download all, even marked as read
			False, # archive after download
			True # prepend date to filename
		)