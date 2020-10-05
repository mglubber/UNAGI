"""
log.py
Date: 2017/06/21
Author: Jung Nicolas
Description: A simple log system
"""

# Native imports
import os
import time


def timestamp():
	return time.strftime("%Y/%m/%d - %H:%M:%S")


class logger:
	logerror = False
	silent = False
	verbose = False
	logfile = None

	def __init__(self, logfile=None):
		self.logfile = logfile
		if logfile is None:
			self.logfile = os.path.join(os.path.dirname(__file__), "log", "main.log")

	def tell(self, string, logfile=None):
		self.write(string, logfile, not self.silent)

	def write(self, string, logfile=None, display=None):
		message = f"[{timestamp()}] {string}"
		if logfile is None:
			logfile = self.logfile
		if display is None:
			display = self.verbose and not self.silent
		if display:
			print(message)
		if not self.logerror:
			try:
				with open(logfile, "a") as log:
					log.write(message + "\n")
			except Exception:
				print(f"Could not write to the log file {logfile}.")
				self.logerror = True

	def erase(self, logfile=None, display=None):
		if logfile is None:
			logfile = self.logfile
		if display is None:
			display = self.verbose
		if display:
			print(f"[{timestamp()}] resetting the logfile {logfile}")
		if not self.logerror:
			try: # TODO: just delete the file, we don't need it
				with open(logfile, "w") as log:
					log.write("")
			except Exception:
				print(f"Could not write to the log file {logfile}.")
