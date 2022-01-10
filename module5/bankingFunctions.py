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