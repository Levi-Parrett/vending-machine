
#creates a class object for each item in the vending machine
class ItemVend:
	def __init__(self, price, capacity, productName):
		self.price = price
		self.maxCapacity = capacity
		self.productName = productName
		self.capacity = self.maxCapacity
	def buy(self,credit):			#action for if a person were to buy an item
		if credit>= self.price and self.capacity >0:
			self.capacity-=1
			credit-=self.price
			return credit	
		elif self.capacity <=0:
			return 'Out of Stock. Please try another selection.'
		else:
			return 'Insufficient Funds'
	def restock(self, n):		#refills inventory
		if self.capacity+n>self.maxCapacity:
			self.capacity=self.maxCapacity
			print('we had excess product')
		else:
			self.capacity+=n
	def reprice(self,Price):	#allows for the change of price in an item
		self.price = Price
	def replace(self,price, capacity, productName): #changing/replacing a product with another
		self.price = price
		self.maxCapacity = capacity
		self.productName = productName
		
