from actions.GetApps import GetApps
from actions.GetBlueprints import GetBlueprints

import sys

def main():
	print( "Maacho Acc acc cho")
	apps = GetApps()
	apps.fetch()
	if sys.version_info > (2, 7, 15):
		print ("Only python version 2.7.15 or lower supported")

if __name__ == "__main__":
	main()
