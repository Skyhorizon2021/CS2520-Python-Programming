"""
We're working on an inventory management system for our hotel to track items like food or toiletries. We want to create stock alerts.

In our system, we specify low and high inventory levels, and we will create an alert when a transaction:
* Changes the inventory from above or equal to the low level to below the low level
* Changes the inventory from below or equal to the high level to above the high level
* Results in a negative inventory. This includes going from negative to negative

A transaction can only generate one alert. See the last transaction in the example.

For example, consider the following test case:

Initial inventory = 300, low inventory alert at 100, high inventory alert at 1000
Transaction log: [-100, -150, -20, -50, -20, 100, 1050, -100, -1100]

Initial   Transaction  New Inventory  Alert?
  300         -100          200       No alert
  200         -150           50       Alert     moves from above to below low inventory
   50          -20           30       No alert  was already below low inventory
   30          -50          -20       Alert     results in negative inventory
  -20          -20          -40       Alert     results in negative inventory
  -40          100           60       No alert  was already below low inventory
   60         1050         1110       Alert     moves from below to above high inventory
 1110         -100         1010       No alert  was already above high inventory
 1010        -1100          -90       Alert     results in negative inventory and moves from
                                                above to below low inventory. *Only alerts once*

This results in 5 alerts.

Write a function that takes in an initial inventory, low inventory alert amount, high inventory alert amount, and a list of transactions and returns how many alerts should occur.

log_1  = [-100, -150, -20, -50, -20, 100, 1050, -100, -1100]
log_2  = [-500, 100, 900, -1100, -100, 1200, -1300, 1400]
log_3  = [750, -540, 460, -180, 320, -830, 10, -260, -460, -900, 710, 500, -860, 580, -40]
log_4  = [-170, 860, -40, -190, -600, 30, 670, 310, -590, 1000, -390, -280, 50, -660]
log_5  = [840, -620, -70, -30, -390, 540, -420, 640, 510, 300, 140]
log_6  = [10, -590, -430, -740, -10, 10, 0, -90, -480]
log_7  = [-330, 130, 430, 520, 570]
log_8  = [10, -50, -500, -20, -70, 660, -220, -510, 940, -340]
log_9  = [200, 10, -510, -10, -190, -1, 702, -502]
log_10 = [-200, 125, 300, -500, 1000]

All test cases:
#      Init   Low  High    Log
alerts( 300,  100, 1000, log_1)  => 5
alerts( 500,    0, 1000, log_2)  => 4
alerts(1340,  900, 1500, log_3)  => 4
alerts(1080,  700, 1300, log_4)  => 2
alerts( 470,  400, 1100, log_5)  => 4
alerts( 180,  100,  400, log_6)  => 8
alerts( 940,  800, 1100, log_7)  => 2
alerts(1010,  300, 1300, log_8)  => 0
alerts( 500,  200,  700, log_9)  => 5
alerts( 100,   50,  200, log_10) => 4

Complexity variables:
N = the number of items in the log

"""

log_1 = [-100, -150, -20, -50, -20, 100, 1050, -100, -1100]
log_2 = [-500, 100, 900, -1100, -100, 1200, -1300, 1400]
log_3 = [750, -540, 460, -180, 320, -830, 10, -260, -460, -900, 710, 500, -860, 580, -40]
log_4 = [-170, 860, -40, -190, -600, 30, 670, 310, -590, 1000, -390, -280, 50, -660]
log_5 = [840, -620, -70, -30, -390, 540, -420, 640, 510, 300, 140]
log_6 = [10, -590, -430, -740, -10, 10, 0, -90, -480]
log_7 = [-330, 130, 430, 520, 570]
log_8 = [10, -50, -500, -20, -70, 660, -220, -510, 940, -340]
log_9 = [200, 10, -510, -10, -190, -1, 702, -502]
log_10 = [-200, 125, 300, -500, 1000]

#var to store current inventory, var to store previous inventory 
#1 function to check and alert for low inventory, the same for high inventory

def alertCount(initialInventory, lowInventoryThreshold, highInventoryThreshold, transactionsList):
    numOfAlert = 0
    #loop through transactions
    for transactions in transactionsList:
        newInventory = initialInventory + transactions
        print("Old",initialInventory)
        print("New",newInventory)
        #assign state to initial
        if initialInventory < lowInventoryThreshold:
            initState = "low"
        elif initialInventory > highInventoryThreshold:
            initState = "high"
        else:
            initState = "normal"
        #assign state to new
        if newInventory < lowInventoryThreshold:
            newState = "low"
        elif newInventory > highInventoryThreshold:
            newState = "high"
        else:
            newState = "normal"

        #check from high to low
        if newState == "low" and initState != "low":
            numOfAlert += 1
        #check from low to high
        elif newState == "high" and initState != "high":
            numOfAlert += 1
        #check from negative to negative
        elif newState == "low" and newInventory < 0:
            numOfAlert += 1
        print(numOfAlert)
        
        initialInventory = newInventory
    return numOfAlert

print(alertCount(300,100,1000,log_1))