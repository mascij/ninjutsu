import globals
from NinjaKnife import NinjaKnife
import random
import datetime


class CreateBlueprint(NinjaKnife):

	Name = "Create Blueprint"

	def __init__(self):
		NinjaKnife.__init__( self , NinjaKnife.Post, globals.BLUEPRINTS )
		self.body = globals.NEW_BLUEPRINT

	def fetch(self):
		# Append name random 5 digit number
		self.body += "\"name\":\"Nin-"+ ''.join(random.sample('0123456789', 5))+"\""
		# Append description with created time. 
		self.body += ",\"description\": \"This VM was created at "+ \
			datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+ ".\"}"
		NinjaKnife.fetch(self)

