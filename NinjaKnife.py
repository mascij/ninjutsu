# -*- coding: utf-8 -*-
import globals
import httplib
import json
import base64
import ssl

class NinjaKnife():
	Get  =  "GET"
	Post =  "POST"

	def __init__( self, method, apiurl):
		self.method = method
		self.apiurl = apiurl
		
	def fetch(self, params = ""):
		self.params = params
		conn = httplib.HTTPSConnection(globals.SERVER_URL) 
		conn._context.check_hostname = False 
		conn._context.verify_mode = ssl.CERT_NONE
		headers = {}
		headers["Authorization"] = "Basic %s" % base64.standard_b64encode(globals.PASS_PHRASE)
		req = conn.request(self.method, self.apiurl, headers=headers)
		res = conn.getresponse()
		if res.status == 200:
			parsed = json.loads( res.read())
			print json.dumps(parsed, indent=4, sort_keys=True)
		else:
			print res.status, "Error returned in Response to the Request sent"
		
	


