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