#functions

def menu(menuItems):
	for index in range(len(menuItems)):
		print("{}. {}".format(index+1,menuItems[index]))
        
def getInput(menuList):
    numberOfOptions = len(menuList)
    userInput = int(input("Choose an Option : "))
    if userInput>0 and userInput<=numberOfOptions:
        return userInput
    else:
        return "chooses correct option"
    
def checkBalance(balance):
    print("Current Balance : {}".format(balance))
    
def addBalance(balance):
    addAmount = int(input("enter amount to add : "))
    if (addAmount>0):
        balance += addAmount
    else:
        print("Add amount should not be negative")
        
    print("Current Balance: {}".format(balance))
    return balance
    
def withdrawBalance(balance):
    withdrawAmount = int(input("enter amount to withdraw : "))
    if withdrawAmount>0 :
        if withdrawAmount<=balance:
            balance -= withdrawAmount
        else:
            print("withdraw amount should not be greater than avaialable balance")
    else:
        print("withdraw amount should not be negative")
        
    print("Current Balance: {}".format(balance))
    return balance