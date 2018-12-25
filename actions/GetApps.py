import globals
from NinjaKnife import NinjaKnife


class GetApps(NinjaKnife):

	Name = "Get Apps"

	def __init__(self):
		NinjaKnife.__init__(self, NinjaKnife.Get, globals.GET_APPS )

	def fetch(self):
		NinjaKnife.fetch(self)

