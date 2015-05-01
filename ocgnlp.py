#!/usr/bin/python
# coding: utf-8

"""
Main script for ocgquerygen quepy.
"""

import sys
import time
import random
import datetime
import quepy
import os
import subprocess

ocgquerygen = quepy.install("ocgquerygen")

def get_query(query):
	target, query, metadata = ocgquerygen.get_query(query)
	
	if query:
		cmd="d2rq/d2r-query -f json mapping.n3 \' " + query + "\' > out.json"
		os.system(cmd)
		f = open('out.json','r')
		result = f.read()
		f.close()
		return result
	#else:
	# 	return "Not Query Generated. :("
	#return query
