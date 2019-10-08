import sys

def get_capital(state):
	if len(state) < 1:
		exit()
	if state[0] == "New" and len(state) == 2:
		str_state = state[0] + " " + state[1]
	elif len(state) > 1:
		exit()
	else:
		str_state = state[0]

	if str_state in states:
		print(capital_cities[states[str_state]])
	else:
		print("Unknown state")

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
	get_capital(sys.argv[1:])
