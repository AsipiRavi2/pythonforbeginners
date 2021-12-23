#cars = ["BMW","HONDA","TATA"]
#for car in cars:
#	print(car)
#x = int(input("enter a int:"))
#while x==5:
#    if x%2==0:
#        print("in if {}".format(x))
#    else:
#        print("in else {}".format(x))
#        x = x-1

#cars = ["BMW","HONDA","TATA"]
#for car in cars:
#    print(car)
#    for letter in car:
#        if letter=="A":
#            print(letter)
#           

#for i in range(1,5,1):
#    print(i)
#    if i%2==0:
#        break
#    else:
#        continue

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')