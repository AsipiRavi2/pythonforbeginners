x = 5 

def sum():
    #global x
    x = 7
    print('in fun',x,id(x))
	
sum()

print('out fun',x,id(x))