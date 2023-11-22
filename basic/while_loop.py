i  = int(input("Enter a new number"))

while (i<=40):
    i = int(input("Enter a second new number"))
    print(i)
print("Done with the loop") ## this print will occur once the condition gets false

## in the while loop  it doesnot stop untill it gets false as per the given condition

j = int(input("Enter a number for the loop"))
while(j>10):
    print(j)
    j=j-2
else: 
    print("After the 'while' condition is over I am inside else")