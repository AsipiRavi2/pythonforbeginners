#Banking Application
import bankingFunctions as BF

print("###################\nWelcome to ABSA \n###################\n")
menuList = ["Check Balance","Add Balance","Withdraw Balance","Exit"]
balance = 0

while True:
    BF.menu(menuList)
    userInput = BF.getInput(menuList)
    
    if userInput == 1:
        BF.checkBalance(balance)
    elif userInput == 2:
        balance = BF.addBalance(balance)
    elif userInput == 3:
        balance = BF.withdrawBalance(balance)
    else:
        break

