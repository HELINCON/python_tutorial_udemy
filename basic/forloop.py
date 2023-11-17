# normal loop

numbers = [1,2,3,4,5,6,7,8,9]

for i in numbers:
    print(i)
    if i < 4:
        print("enter more")
    else :
        print("limit sxceeded")
        break
# for spescific limit set

for i in range(numbers[0], numbers[7]):
    print("second loop",i,numbers[7]) # here the output of i will be till 7th index 
                                      #  as last limit is numbers[7] whose value is 8