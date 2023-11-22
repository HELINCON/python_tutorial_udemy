# required argument
def new(a,b):
    print("average::", (a+b)/2)   # it gives rounded result as '/' is used
                                  # a and b are required argument as it doe not have a default value
new(4,2)

# ----------------------------------------------------------
# default argument
def default(a=4,b=7):
    float_value = (a+b)/2
    rounded_value = (a+b)//2
    print("rounded_value:",rounded_value)
    print("float_value:",float_value)

default() 
default(111,8)    # but if we provide new arguments to the function then it will ignore a=4 and b=7
default(a=17)     # here a value will be 17 and b value will that same 7
default(b=127)    # here b value will become 127 and a value will be same 4

# -----------------------------------------------------------
# keyword arguments
def keyword(a=4,b=7):
    float_val = (a+b)/2
    round_val = (a+b)//2
    print("float_val:",float_val)
    print("round_val:",round_val)
    
keyword(b=8, a=18) # here argument position is changed still funtion will take the argument as per the arguments name

# -------------------------------------------------------------
# variable_length_argument

def variable_length_argument(*numbers):
    sum = 0
    for i in numbers:
     print(i)
     sum = sum + i 
     print(numbers)
    print("average in variable_length_argument is :",sum/len(numbers) )
    
variable_length_argument(5,6)



def newfunc(*numbers):   # here the arguments are wrapped into a tuple and passed into the function
    sum = 0
    print("=====",type(numbers))
    
    for i in numbers:
        sum = sum +i
        print("i:",i)
        new_tup = numbers + (70,80)   # here numbers are added to a tuple by adding and asssigning to a new tuple variable
        print(type(new_tup))
        print("new_tup", new_tup)
        
    print("summation of all the numbers", sum,numbers)
        
newfunc(10,20,30,40,50)

# trick to replace or add data in a tuple without assigning it's original value to a new variable

new_tuple = (1,2,3,4,5)
lis = list(new_tuple)
lis.extend([6,7,8])
new_tuple = tuple(lis)
print("cdgycdycydc--->",new_tuple)

# ------------------------------------------------------
# keyword_arbitrary_arguments


def name(**name):
    print(type(name))
    print("name", name)
    print("Hello", name["fname"],
          name["mname"],name["lname"])

    
name(mname="X", fname = "M", lname = "Helincon") # here arguments are passed as per the position as it happens usually

# in the above code only these tyoe of arguments can be passed but a positional argument cannot be passed.


