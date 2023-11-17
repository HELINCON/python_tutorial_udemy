patient = "john players"
age = 20
# print("user details--------->"+patient, age)

new_patient = {patient, age}
new_patient2 = patient,age
print(new_patient)   # here the answer will be {20, 'john players'}  first int then string
print(new_patient2)  # but here the answer will be ('john players', 20) first string then int

# name = input("what is your name")
# print("hello", name)

clas = input("what is your class  ")
# print("my class is ",clas)

birth_year = input("enter the birthday year ")
age = 2023 - int(birth_year)
print("the age is",age)

side_name = "frankok"
print(side_name.find("k"))
print("the data type of side name is ==> " , type(side_name))  
# string cannot concatenate with type in python so instead of "+" rather "," is used 
# print(side_name.replace(side_name, "frankok got replaced to a this sentence written now"))
print(side_name.replace("male", "a friend of frankok charlie"))
print(side_name)

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[16:13:-1]
print(backwards)
newbackwards = letters[24:16:-3]
print(newbackwards)



