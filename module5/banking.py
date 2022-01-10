#Banking Application
import bankingFunctions

print("###################\nWelcome to ABSA \n###################\n")
menuList = ["Check Balance","Add Balance","Withdraw Balance","Exit"]
balance = 0

bankingFunctions.menu(menuList)
userInput = bankingFunctions.getInput(menuList)

if userInput== 1:
    bankingFunctions.checkBalance(balance)
else:
    print('options not working')

