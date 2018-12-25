import globals
import httplib
import urllib


class NinjaKnife():
	Get     =	"GET"
	Post 	=   "POST"

	def __init__( self, method, apiurl):
		self.method = method
		self.apiurl = globals.SERVER_URL+apiurl

	def fetch(self, params = ""):
		self.params = params
		print("hello world"+ params);

