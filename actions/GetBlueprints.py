import globals
from NinjaKnife import NinjaKnife

class GetBlueprints(NinjaKnife):

	Name = "Get Blueprints"

	def __init__(self):
		NinjaKnife.__init__( self , NinjaKnife.Get, globals.GET_BLUEPRINTS )

	def fetch(self):
		NinjaKnife.fetch(self)

	