import sys

def getvalue(string, index):
	return string[index].split(":")[1]

def read(file):
	strTable = "<html><table>" #<tr><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th></tr>"
    
	list_elements = []

	f = open(file, "r")
	f1 = f.readlines()
	for line in f1:
		attributes = line.split(",")
		name = attributes[0].split("=")[0]
		electrons = getvalue(attributes, 4)
		electrons = list(electrons.split(" "))
		electrons = list(map(int, electrons))
		element = {
			"name":name,
			"position": int(getvalue(attributes, 0)),
			"number": getvalue(attributes, 1),
			"symbol": getvalue(attributes, 2),
			"molar": getvalue(attributes, 3),
			"electrons": sum(electrons)
		}
		list_elements.append(element)
	fill_table(list_elements, strTable)


def fill_cell(elem):
	attributes = "<td style='border: 1px solid black; padding:10px'><h4>"+str(elem["name"])+"</h4>"+"<ul><li> No: "+str(elem["number"])+"</li><li>"+str(elem["symbol"])+"</li><li>"+elem["molar"]+"</li><li>"+str(elem["electrons"])+" elec</li></ol></td>"
	return attributes

def fill_table(list_elements, strTable):
	# take first position

	for x in range(8):
		strCell = "<tr>"
		for y in range(18):
			# strCell = ""
			if len(list_elements) < 1:
				continue
			else:
				elem = list_elements[0]
			print(y)
			print(elem["position"])
			if y == elem["position"]:
				strCell = strCell + fill_cell(elem)
				list_elements = list_elements[1:]
			else:
				print("why does it not go here")
				strCell = strCell + "<td></td>"
				print(strCell)
		strLine = strCell + "</tr>"
		strTable = strTable + strLine
	strTable = strTable+"</table></html>"
	print(strTable)
	hs = open("periodic_table.html", 'w')
	hs.write(strTable)

if __name__ == '__main__' :
	read("periodic_table.txt")