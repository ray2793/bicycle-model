"""
Create a bicycle shop that has 6 different bicycle models in stock. The shop should charge its customers 20% over the cost of the bikes.
Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. Make sure you price the bikes in such a way that each customer can afford at least one.
Print the initial inventory of the bike shop for each bike it carries.
Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.
"""

class Bicycle (object):
    
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        self.price = cost * 1.2
        
class BikeShop (Bicycle):
    
    def __init__(self, name, bikes):
        self.name = name
        self.profit = 0
        self.inventory = {}
        #Iterates through bikes set and puts bike objects in inventory dictionary with bike model as key
        for bike in bikes:
            self.inventory[bike.model] = bike
    
    #Takes bike object (values) from inventory dict, compares price of bike against input fund, returns LIST (since comprehension) of bikes
    def filter (self, funds):
        bikes = self.inventory.values()
        return [bike for bike in bikes if bike.price <= funds]

    def sell(self, bike):
        self.profit += (self.inventory[bike.model].price - self.inventory[bike.model].cost)
        self.inventory.pop(bike.model)
        print ('{} just sold a {}! '.format(self.name, bike.model))

class Customers(BikeShop):
    
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.potentialbikes = {}
        self.ownedbikes = []
        self.affordables = []
    
    def printpotentialbikes(self):
        print (self.name + ' can afford: ' + ', '.join(self.potentialbikes))
    
    def buy(self, bikeshop, bike):
        self.ownedbikes.append(bike)
        self.fund -= bike.price
        print ('{} just bought a {} for ${:.0f} and has ${:.0f} left'.format(self.name, bike.model, bike.price, self.fund))
        bikeshop.sell(bike)

        
        
        
        
    


        