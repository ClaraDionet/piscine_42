import random
import beverages

class CoffeeMachine:
	def __init__(self):
		self.count = 0
	class EmptyCup(beverages.HotBeverage):
		name = "empty cup"
		price = 0.90
		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self, msg= "This coffee machine has to be repaired."):
			# self.msg = msg
			super().__init__(self, msg)

	def repair(self):
		self.count = 0
		print("Machine repaired")

	def serve(self, bev):
		rand = random.randint(0,1)
		empty = self.EmptyCup()
		if self.count < 10:
			if rand == 0:
				self.count += 1
				return(bev)
			else:
				self.count += 1
				return(empty)
		else:
				raise self.BrokenMachineException()

beverages = {0: beverages.HotBeverage(), 
			1: beverages.Coffee(), 
			2: beverages.Tea(), 
			3: beverages.Chocolate(), 
			4: beverages.Cappuccino()}
cm = CoffeeMachine()
for i in range(30):
	rand_bis = random.randint(0,4)
	try:
		print(cm.serve(beverages[rand_bis]))
	except Exception as e:
		print(str(e))
		cm.repair()







