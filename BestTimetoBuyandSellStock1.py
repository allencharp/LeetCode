# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions 
# as you like (ie, buy one and sell one share of the stock multiple times). However, 
# you may not engage in multiple transactions at the same time (ie, you must sell the 
# stock before you buy again).
class Stock():
	
	def __init__(self):
		self.min = max
		self.max = 0
		self.currentprofit = 0

class Solution:
	def maxProfit(self, prices):
		if(len(prices) == 0):
			return 0
	

		stock = Stock()
		for i in range(len(prices)):
			
			price = prices[i]
			
			if (i == 0):
				stock.min = price
				stock.currentprofit = 0
				continue;

			if( price > stock.min):
				if (price - stock.min > stock.currentprofit):
					stock.max = price
					stock.currentprofit = price - stock.min
					
			else:
				stock.min = price
				stock.max = 0

		return stock.currentprofit