"""
Create a bicycle shop that has 6 different bicycle models in stock. The shop should charge its customers 20% over the cost of the bikes.
Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. Make sure you price the bikes in such a way that each customer can afford at least one.
Print the initial inventory of the bike shop for each bike it carries.
Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.
"""

class Bicycle(object):
    
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
class BikeShop (object):
    
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    
    #def sell(self):
        #TBD
    
    #def calcprofit(self):
        #TBD

class Customers(object):
    
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
    
    #def buy(self):
        
    

        