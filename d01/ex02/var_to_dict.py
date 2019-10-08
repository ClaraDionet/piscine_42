def var_to_dict(d):
	dic = dict(d)
	inv_dic = {}
	for k, v in dic.items():
		if v in inv_dic:
			inv_dic[v].append(k)
		else:
			inv_dic[v] = [k]
	for k,v in inv_dic.items():
		str_v = ""
		for v in inv_dic[k]:
			str_v += " " + v
		print(k, ":", str_v)

if __name__ == '__main__' :
	d = [
	('Hendrix' , '1942'),
	('Allman' , '1946'),
	('King' , '1925'),
	('Clapton' , '1945'),
	('Johnson' , '1911'),
	('Berry' , '1926'),
	('Vaughan' , '1954'),
	('Cooder' , '1947'),
	('Page' , '1944'),
	('Richards' , '1943'),
	('Hammett' , '1962'),
	('Cobain' , '1967'),
	('Garcia' , '1942'),
	('Beck' , '1944'),
	('Santana' , '1947'),
	('Ramone' , '1948'),
	('White' , '1975'),
	('Frusciante', '1970'),
	('Thompson' , '1949'),
	('Burton' , '1939')
	]
	var_to_dict(d)

 

