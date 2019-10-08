def print_type(var):
	print(var, "est de type", type(var))


def my_var():
	print_type(42)
	print_type("42")
	print_type("quarante-deux")
	print_type(42.0)
	print_type(True)
	print_type([42])
	print_type({42:42})
	print_type((42,))
	print_type(set())	

if __name__ == '__main__' :
    my_var()