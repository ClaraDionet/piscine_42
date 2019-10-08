import sys 

def get_key(dic, search_value):
	for k,v in dic.items():
		if v == search_value:
			return k

def get_state(capital):
	if len(capital) != 1:
		exit()
	else:
		if get_key(capital_cities,capital[0]) != None:
			print(get_key(states,get_key(capital_cities,capital[0])))
		else:
			print("Unknown capital city")

def all_in(lstr):
	# split with comma
	lstr = lstr.split(",")
	# remove empty/space elements
	lstr = list(filter(str.strip, lstr))
	# remove beginning whitespace
	lstr = [x.lstrip() for x in lstr]

	# print(lstr)
	for element in lstr:
		element_cap = element.title()

		# check if element is a state
		if element_cap in states:
			print(capital_cities[states[element_cap]] + " is the capital of " + element_cap)
		# else check if element is a capital
		elif get_key(capital_cities,element_cap) != None:
			print(element_cap + " is the capital of " + get_key(states,get_key(capital_cities,element_cap)))
		else:
			print(element + " is neither a capital city nor a state")

if __name__ == '__main__' :
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	all_in(sys.argv[1])


