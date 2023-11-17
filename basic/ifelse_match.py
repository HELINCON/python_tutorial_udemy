import time

current_time = time.strftime('%H:%M:%S')

print(current_time)

a = 20
if a != 20:
    print("This is working")
elif current_time == "yes":
    print("This is not working")
else: 
    print("kadali")


x = int(input("Enter a number "))
print(type(x))

match x:
    case 0:                             ## in match case it only checks for a condition, if satisfies then stops from there.
                                        ## it doesnot wait for a break
        print("the matched value is 0")
    case _ if x == str or x!= None:
        print("if x == str or x!= None:", x)
    case _ if x == str:
        print(" third case", x)