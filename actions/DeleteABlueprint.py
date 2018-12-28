import globals
from NinjaKnife import NinjaKnife

class DeleteABlueprint(NinjaKnife):

	Name = "Delete a Blueprint"

	def __init__(self):
		NinjaKnife.__init__( self , NinjaKnife.Delete, globals.BLUEPRINTS)

	def fetch(self, params=""):
		self.apiurl = globals.BLUEPRINTS +"/"+ params #redundant assignment :((
		NinjaKnife.fetch(self)

