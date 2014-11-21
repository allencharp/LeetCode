# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell 
# one share of the stock), design an algorithm to find the maximum profit.

class Stock():
	
	def __init__(self):
		self.min = max
		self.max = 0
		self.profit = []

class Solution:
	def maxProfit(self, prices):		
		if(len(prices) == 0):
			return 0
	
		stock = Stock()
		for i in range(len(prices)):
			
			price = prices[i]
			
			if (i == 0):
				stock.min = price
				stock.profit = []
				continue;

			if( price > stock.min):
				stock.profit.append(price - stock.min)
				stock.min = price
				
			else:
				stock.min = price
				
		stock.profit = stock.profit + [0,0] # for the cases profict is empty or less than 1
		return reduce(lambda x, y: x+y, stock.profit)