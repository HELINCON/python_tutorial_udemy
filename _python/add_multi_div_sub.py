first_num = int(input("Enter first number"))
second_num = int(input('Enter second number'))
operation = input("Entrer operation condition")
# result = (first_num , second_num , operation)
if operation == '+':
    print("result is",first_num+second_num)
elif operation == '-':
    print("result is",first_num-second_num)
elif operation == '*':
    print("result is",first_num*second_num)
elif operation == '//':
    print("result is",first_num//second_num)
elif operation == '/':
    print("result is",first_num/second_num)
