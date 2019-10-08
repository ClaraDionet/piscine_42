class HotBeverage:
	price = 0.30
	name = "hot beverage"
	# def __init__(self, price = 0.30, name = "hot beverage"):
	# 	self.price = price
	# 	self.name = name
	def description(self):
		return "Just some hot water in a cup."
	def __str__(self):
		return " name : " + self.name + "\n price : " + str(self.price) + "\n description : " + self.description()

class Coffee(HotBeverage):
	name = "coffee"
	price = 0.40

	def description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverage):
	name = "tea"

class Chocolate(HotBeverage):
	name = "chocolate"
	price = 0.50

	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	name = "capuccino"
	price = 0.45

	def description(self):
		return "Un po’ di Italia nella sua tazza!"

if __name__ == '__main__' :
	hb1 = HotBeverage()
	print(hb1)

	hb2 = Coffee()
	print(hb2)

	hb3 = Tea()
	print(hb3)

	hb4 = Chocolate()
	print(hb4)

	hb5 = Cappuccino()
	print(hb5)
