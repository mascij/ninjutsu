from actions.GetApps import GetApps
from actions.GetBlueprints import GetBlueprints

import sys

def main():
	if sys.version_info > (2, 7, 17):
		raise Exception ("Only python version 2.7.17 or lower supported")
	apis = { "1" : "Get Blueprints", "2" :"Get Apps"}
	objects = { "1" : GetBlueprints(), "2" : GetApps()}
	var ="0"
	while True:
		print("##############################################################\n\r")
		for key in apis:
			print key," ",apis[key]
		var = raw_input("\n.................Please enter your choice\n\r")
		if var not in apis.keys():
			print "Invalid Selection.. Exiting"
			break
		else:
			callObject = objects[var]
			callObject.fetch()
			continue


if __name__ == "__main__":
	main()
