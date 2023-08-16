# ram ram

a=12
b=3
print("a / b ==> ",a/b)            # answer - 4.0
print("a // b ==> ",a // b)        # answer - 4 integer division ,rounded down towards minus infinity
print("a % b ==> ",a % b)          # answer - 0 modulo: the remainder after integer division

c = 16
d = 5
print("c // d ==> ",c // d)        # answer - 3 rounded down towards minus infinity 
                                   # but it takes a lot of time and all are computed at the same time.
for i in range(1, 4):
 if i < 2:
    print(i,"st loop")
else:
        print(i,"nd loop")                         

for i in range( 1, a // b ):        # here we cannot type (a / b) as it will give float result 
    print(i)                        # and integer(1) cannot be computed with second argument which is a float amount
                                    # that's why we gave a // b as its result will be a rounded one

# in Javascript we give condition for a for loop    ((let i=o, i < array.length, i++ ))
# but in python we give the range                   ((starting point of iteration , ending point of iteration))