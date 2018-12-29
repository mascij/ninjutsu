from actions.GetApps import GetApps
from actions.GetBlueprints import GetBlueprints
from actions.CreateBlueprint import CreateBlueprint
from actions.DeleteABlueprint import DeleteABlueprint

import sys

def main():
	if not sys.version_info[0] == 2 and sys.version.info[1] == 7:
		raise Exception ("Only python version 2.7.x supported")
	apis = { 1 : GetBlueprints(), 2 : GetApps(), 3 : CreateBlueprint(), 4: DeleteABlueprint()}
	choice ="0"
	while True:
		print("##############################################################\n\r")
		for key in apis:
			print key," ",apis[key].Name
		try:
			choice = int(raw_input("\nEnter option 1 - 4 : "))
			if choice not in apis.keys():
				raise ValueError()
			if choice == 4:
				id = (raw_input("Enter the Blueprint id to delete : "))
				apis[choice].fetch(id)
			else:
				apis[choice].fetch()
			continue
		except ValueError as err:
			print "Invalid option or bad entry ... exiting.."
		except StandardError as err:
			print str(err),"Appears your internet is down. Fix internet and try again"
		exit(0)

if __name__ == "__main__":
	main()



