
#https://stackoverflow.com/questions/38189660/two-variables-in-python-have-same-id-but-not-lists-or-tuples
#+,-,*,/,%,**,//
print(5+4**2*2)
BODMAS



name = "ravi"
x = 5 #110 = 1*2^2+1*2^1+0*2^0 = 4+2+0
y = 5 #101 = 1*2^2+0*2^1+1*2^0 = 4+0+1


#==,>,<,!=,>=,<=

#and, or, not

#is, is not 

# in, not in 

#&,|, ^, ~, <<, >>

#&
print(x&y) #100 = 4

#&
print(x|y) #111 = 7

#^
print(x^y) #011 = 3 

#~
print(~x) #

#>>

print(x>>2)

#>>
print(x<<2)
print(x)



#in 
print("x" in name) # True
#not in 
print("i" not in name) #False

#and
print(id(x),id(y))
print(x is y) #false
print(x==y)
# or
print(x is not y) # true
print(x!=y)

#and
print(x==8 and y==4) #false

# or
print(x==8 or y==4) # true

# not
print(not x==8) # false

# ==
print(x==y) #false

# >
print(x>y) # true

#<
print(x<y) # false

# !=
print(x!=y) # true

#>=
print(x>=y) # false

# <=
print(x<=y) # false

# addition
print(x+y)

# substraction
print(x-y)

#Multiplication
print(x*y)

#division
print(x/y)

#reminder
print(x%y)

#exponential
print(x**y) #7^5

#modulus
print(x//y)
