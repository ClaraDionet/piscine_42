def read_write(file):
	f = open(file,"r")
	f1 = f.readlines()
	for x in f1:
		print(x.replace(",","\n"))

if __name__ == '__main__' :
    read_write("numbers.txt")