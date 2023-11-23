# in tuple data are constant and new data can not be assigned

tup = (1,2,3,4,5,"green", True)
print(type(tup))
# tup[0] = 2 
# this above code will throw error as a new value cannot be assigned or values cannot be replaced in a tuple


print(tup[0]) # this will gie the first index value of the tuple
print(tup[-2]) # this will give the value as per len(tup)-2


if "green" in tup:
    print("yes green is present in tup")
    
tup1 = tup[1:4]
print(f"result of tup1: {tup1}")

tup3 = (1,2,3,4,5)
tup4 = (6,7,8,9,10)

print(f"concaneted tuple is {tup3 + tup4}")
concat_tup = tup3 + tup4
print(f"concanated tuple is: {concat_tup}")
print("-------------------------------------------------")
# --------------------------------------------------------------------------------------------
# either convert to list , append and then convert it to tuple or else concat
#---------------------------------------------------------------------------------------------
tup5 = ("china","japan","russia")
temp = list(tup5)
temp.append("India")
print(f"the new list is : {temp}")
tup5 = tuple(temp)
print(f"the new tuple is : {tup5}")

# or
print("-----------------OR--------------------")

temp_tup = ("India","srilanka")
con_Tup = tup5+temp_tup
print(f"concanated tuple of countries is : {con_Tup}")

# count and index
tupl = (1,2,4,5,3,3,4,5,2,3,5,3,4,2,5,3,4)
req = 5
print(f"the count of {req} in tupl is: {tupl.count(req)}")
print(f"the index of {req} in tupl is: {tupl.index(req)}")