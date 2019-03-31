"""
Create a bicycle shop that has 6 different bicycle models in stock. The shop should charge its customers 20% over the cost of the bikes.
Create three customers. One customer has a budget of $200, the second $500, and the third $1000.
Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. Make sure you price the bikes in such a way that each customer can afford at least one.
Print the initial inventory of the bike shop for each bike it carries.
Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.
"""

from bicycles import Bicycle, BikeShop, Customers

if __name__ == '__main__':

    #Create a bicycle shop that has 6 different bicycle models in stock. The shop should charge its customers 20% over the cost of the bikes.
    
    bikes = {
        Bicycle("cheetahbike", 10, 50), Bicycle("catbike", 25, 100),
        Bicycle("dogbike", 50, 200), Bicycle("turtlebike", 75, 300),
        Bicycle("birdbike", 100, 500), Bicycle("capybike", 200, 1000)
    }
    
    # cheetahbike = Bicycle("cheetahbike", 10, 50)
    # catbike = Bicycle("catbike", 25, 100)
    # dogbike = Bicycle("dogbike", 50, 200)
    # turtlebike = Bicycle("turtlebike", 75, 300)
    # birdbike = Bicycle("birdbike", 100, 500)
    # capybike = Bicycle("capybike", 200, 1000)
    
    jim = Customers('jim', 200)
    oscar = Customers('oscar', 500)
    jan = Customers('jan', 1000)
    
    #instantiate the bike shop and add bikes to inventory dictionary {model: object}
    theoffice =  BikeShop('theoffice', bikes)
    
    #Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. Make sure you price the bikes in such a way that each customer can afford at least one.
    
    for bike in theoffice.inventory:
        if jim.fund >= theoffice.inventory[bike].price:
            jim.potentialbikes[bike] = theoffice.inventory[bike]
        if oscar.fund >= theoffice.inventory[bike].price:
            oscar.potentialbikes[bike] = theoffice.inventory[bike]
        if jan.fund >= theoffice.inventory[bike].price:
            jan.potentialbikes[bike] = theoffice.inventory[bike]  
    
    jim.printpotentialbikes()
    oscar.printpotentialbikes()
    jan.printpotentialbikes()
    
    #Print the initial inventory of the bike shop for each bike it carries.
    print ("\n"+ "Here's what the office has to offer today:")
    for key, value in theoffice.inventory.items():
        print (key)
    print()
    
    jim.buy (theoffice, theoffice.inventory["cheetahbike"])
    oscar.buy (theoffice, theoffice.inventory["catbike"])
    jan.buy (theoffice, theoffice.inventory["turtlebike"])
    
    print ("\n"+ "Here's what the office has left:")
    for key, value in theoffice.inventory.items():
        print (key)
    print ("The office has made ${:.0f}".format(theoffice.profit))
    
    
    #loop through inventory
    #for each customer, print price < funds