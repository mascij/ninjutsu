from actions.GetApps import GetApps
from actions.GetBlueprints import GetBlueprints
import sys

def main():
	if not sys.version_info[0] == 2 and sys.version.info[1] == 7:
		raise Exception ("Only python version 2.7.x supported")
	apis = { "1" : GetBlueprints(), "2" : GetApps()}
	choice ="0"
	while True:
		print("##############################################################\n\r")
		for key in apis:
			print key," ",apis[key].Name
		choice = raw_input("\n.................Please enter a valid choice\n\r")
		if choice not in apis.keys():
			print "Invalid Selection.. Exiting"
			break
		else:
			try:
				apis[choice].fetch()
				continue
			except StandardError as err:
				print str(err),"Appears your internet is down. Fix internet and try again"
				exit(0)

if __name__ == "__main__":
	main()
