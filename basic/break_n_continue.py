print("-----------------------------")
print("Break and continue in python:=>")
print("-----------------------------")

for i in range(12):
    if i>5 and i<=10:
        print("Skip the iteration")   # here because of continue statement written 
        continue                      # below a new iteration is opened as per the given condition
    print("5 x", i,"=", 5*i)

print("Looop finished")