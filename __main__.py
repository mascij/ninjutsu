from actions.GetApps import GetApps
from actions.GetBlueprints import GetBlueprints

import sys

def main():
	if sys.version_info > (2, 7, 17):
		raise Exception ("Only python version 2.7.17 or lower supported")
	apis = { "1" : GetBlueprints(), "2" : GetApps()}
	choice ="0"
	while True:
		print("##############################################################\n\r")
		for key in apis:
			print key," ",apis[key].Name
		choice = raw_input("\n.................Please enter your choice\n\r")
		if choice not in apis.keys():
			print "Invalid Selection.. Exiting"
			break
		else:
			apis[choice].fetch()
			continue

if __name__ == "__main__":
	main()
