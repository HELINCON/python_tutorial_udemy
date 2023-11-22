# normal loop

numbers = [10,2,3,4,5,6,7,8,9]

for i in numbers:
    print(i)
    if i < 88:
        print("enter more")
    else :
        print("limit sxceeded")
        break

print("*********************************************")
# for spescific limit set :
# ------------------------
# in the below function last parameter is the number of elemets to be skipped and this is optional

for i in range(0,numbers[0],2):
    print("value of i:",i) # here the output of i will be till 7th index 
                                      #  as last limit is numbers[7] whose value is 8
                        
# **************************************************************************                                 
print("*******************************8")   

# here inorder to execute a loop agaist a variable the code style is different from javascript
                                   
colors = ["red", "blue", "green", "orange"]



# Example 1: Creating a list of indices
indices = [i for i in range(len(colors))]
print(indices)
for j in indices:
    print("each element",j)


print("**************************")
# Example 2: Creating a list of tuples with index and color
index_color_pairs = [(i, color) for i, color in enumerate(colors)] ## here in (i,color) i is the index 
                                                                    # and color is the element inside the index
print("i",i)
print(index_color_pairs)
single_element = [i for i in range(len(index_color_pairs))]
print("single_element", single_element)

# *******************************************************************
print("*******************************")

ranga = ["red", "blue", "green", "orange"]

for i in ranga:
    print(i)
    for j in i:
        print(j)
        
        
# ******************************************************************
# to catch the result of a loop in variable we can write the loop like this
colors = ["red", "blue", "green", "orange"]

result1 = []  # Initialize an empty list to store the values
result2 = []
for color in colors:
    result1.append(color)
    for char in color:
        result2.append(char)

print("result1:",result1,"result2:",result2)

colors = ["red", "blue", "green", "orange"]

col1 = []  # Initialize an empty list to store the values

for color in colors:
    col1.append(color)
    for char in color:
        col1.append(char)

print("col1:",col1)

print("(******************)")

new_aray = [10,20,30,40,59,60,70]

for i in new_aray:     # in this loop i value is not directly the index but the value assigned to the index
    print(i)

for i in range(0,new_aray[6]):     # here the value is the index
    print(i)