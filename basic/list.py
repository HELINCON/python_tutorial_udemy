classes = [1,2,3,4,5,"text", True] # in list all type of data can be stored
print(type(classes))
print(classes[0])
print(type(classes[0]))

# incase if i have to use negative index then

print(classes[-3])
#OR
print(classes[len(classes)-3])    # both the cases will always return the same value


if "te" in "text":                # though the "text" of list named 'classes' is called for the codition , classes is not required to write
    print("yes it is present")
    

nList = [{"x":int(1)},{"y":str("charlie")}]
print("nlist ========",nList[1]["y"])

if "lie" in "charlie":
    print("yes")
else:
    print("no")
    
newvar = 12

print(type(newvar))

if "text" in classes:
    print("text is there in classes")
else:
    print("text is not there in classes")    


daray = ["charlie","frankok"]

if "charlie" in daray:
    print("yes charlie is there")
else:
    print("no the given word is not there")
    

sclin_nm = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("slicingm[1]:",sclin_nm[1])
print("slicing[1:4]:",sclin_nm[1:4])       # [number,number] 1st index parameter remains present but second parameter not
print("slicing[1:-2]:",sclin_nm[1:-2])      # first turn -2 to positive index.  len(sclin_nm)-2 which becomes [1,6]
print("slicing[0:1]:",sclin_nm[0:1])
print("slicing[1:14:2]:",sclin_nm[1:15:2]) # last parameter is to skip the numbers 2 means skipping two numbers including start

print('-------------------------------------')
# append and extend in list
original_l = [1,5,2,4,6,3,7]
print("original_l",original_l)

appended_l = original_l.copy()    # in python if array is not copied then the original array will be replaced
extended_l = original_l.copy()

ext_req = (8,9,10,11)
extended_l.extend(ext_req)
print("extended_l:", extended_l)

appended_l.append(8)
print("appended_l",appended_l)

# sorting the list : sort()
org_list = [10,50,20,60,40,70,30]

sorted_l = org_list.copy()
sorted_l.sort()                          # this list is sorted. means it will come in ascending order
print("sorted_l in sorted order:",sorted_l)

reversed_l = org_list.copy()
reversed_l.sort(reverse=True)               # this list is reversed sorted. means it will come in descending order
print("extended_l in reverse sorted order:",reversed_l)

#index()
liSt = [{'a':1},{'b':2},{'c':3},{'d':4}]
indices_of_c = [index for index, dictionary in enumerate(liSt) if 'c' in dictionary]
if indices_of_c:
    print(f"The indices of dictionaries containing 'c' are: {indices_of_c}")
else:
    print("Key 'c' not found in any dictionary.")

# ----------------------------------------------------------
# multiply each value of list with 10

# type 1 using charlie's for loop logic
test_l_1 = [1,2,3,4,5]
revised_l = []

for i in test_l_1:
    new_element = i*10
    revised_l.append(new_element)

test_l_1 = revised_l
        
print("replaced test_l_1 after multiplication:",test_l_1)

# type2 using for loop range
test_l_2 = [{"x":1},{"x":2},{"x":3},{"x":4},{"x":5}]
print("type=================",type(test_l_2[0]["x"]))

for i in range(len(test_l_2)):
    test_l_2[i]["x"] =test_l_2[i]["x"]*10
print("replaced test_l_2 after multiplication:", test_l_2)


# type4 using for loop
test_l_3 = [1,2,3,4,5]

test_l_3 = [x*10 for x in test_l_3]
print("replaced test_l_3 after multiplication:",test_l_3)

# -----------------------------------------------

x = "x"
y = "y"
z = "z"
unquoted = [{x:1},{y:2},{z:3}]   # in dictionary we have to define the key . . either there or before.

print(f"unquoted===========>:{unquoted}")


# formatted string 
z = "my name is charlie"

print(f"the answer to his question is {z}")

# count
li = [1,2,1,3,1,4,5]

print(li.count(1))    # it counts the number of the argument's presence inside the list, thre 1 is there. so ans is 3

# concatination of two lists
lis1 = [1,2,3,4,5]
lis2 = [100,200,300,400,500]
print(f"concatinated list is : {lis2+lis1}")
        # OR
concat_list = lis1+lis2
print(f"concatinated list is : {concat_list}")