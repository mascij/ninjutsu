import globals
from NinjaKnife import NinjaKnife


class GetBlueprints(NinjaKnife):

	def __init__(self):
		NinjaKnife.__init__(self,NinjaKnife.Get, globals.GET_BLUEPRINTS )

	def fetch(self):
		NinjaKnife.fetch(self, self.__class__.__name__)



