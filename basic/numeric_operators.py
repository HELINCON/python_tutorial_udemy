# ram ram

a=12
b=3
print("a=12 / b=3 ==> ",a/b)            # answer - 4.0
print("a=12 // b=3 ==> ",a // b)        # answer - 4 integer division ,rounded down towards minus infinity
print("a=12 % b=3 ==> ",a % b)          # answer - 0 modulo: the remainder after integer division

c = 16
d = 5
print("c=16 // d=5 ==> ",c // d)        # answer - 3 rounded down towards minus infinity 
                                   # but it takes a lot of time and all are computed at the same time.

k = 8j 
l = 9j    
print(k)                             
for i in range(1, 7):              # here range is between 1 and 7 and in between them // is mandatory
 if i < 1:
    print(i,"st loop", k+l)
else:
        print(i,"nd loop",k+l)                         

for i in range( 1, a // b ):        # here we cannot type (a / b) as it will give float result 
    print(i)                        # and integer(1) cannot be computed with second argument which is a float amount
                                    # that's why we gave a // b as its result will be a rounded one
                                    # in this loop // determines starting and ending point

# in Javascript we give condition for a for loop    ((let i=o, i < array.length, i++ ))
# but in python we give the range                   ((starting point of iteration , // , ending point of iteration))



complicated = complex(1,2)
print(complicated)