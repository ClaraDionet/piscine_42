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
	get_state(sys.argv[1:])