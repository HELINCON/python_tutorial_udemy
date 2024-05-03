questions = [{"Q1":"what is national bird of India ?"},{"Q2":'What is the national animal of India'},{"Q3":'What is the national flower of India'},{"Q4":'What is the national Tree of India'}]
options = [
           {"Q1":[{"A":"peacock"},{"B":"Pigeon"},{"C":"Crow"},{"D":"Owl"}]},
           {"Q2":[{"A":"Cow"},{"B":"Tiger"},{"C":"Hippopotamus"},{"D":"Dog"}]},
           {"Q3":[{"A":"Daisy"},{"B":"Jasmine"},{"C":"Mariegold"},{"D":"Lotus"}]},
           {"Q4":[{"A":"Banana"},{"B":"Banyan"},{"C":"Palm"},{"D":"Coconut"}]}
           ]

right_answers = [{"Q1":"A"},{"Q2":"B"},{"Q3":"D"},{"Q4":"B"}]
amount = [{"wronganswer":"0"},{"Q1":"1000"},{"Q2":'5,000'},{"Q3":'10,000'},{"Q4":'50,000'}]

Welcome_message = 'WELCOME to KBC. All the best !!'
condolense = 'Oops Wrong answer ! Better Luck next time'
last_money = 'The amount you have earned is: '
congratulations = 'Congratulations. You have won Rs.'
correct_ans = 'Correct answer !'

total_money = amount[1]['Q1']
initial_money = 1


def Q1():
    q_index = 1-1
    print(Welcome_message)
    print(questions[q_index]["Q1"])
    
    target_question = "Q1"
    for question in options:                         # Iterate through the list and print the values for the specified options
     if target_question in question:
        for option in question[target_question]:
            for option_key, option_value in option.items():        # here iteration happens inside the tuple. 
                print(f'{option_key}. {option_value}')                         # first index key and second value
                
    input_ans = (input("Enter the answer in block letter: ")) 
    print("The answer you enterd is: ", input_ans)
    if(input_ans != right_answers[q_index]["Q1"]):
        print(condolense)   
        print("Sorry you could not earn any money")
        return{
            "statement": False
        }
    else:
        print(correct_ans)
        print(f"{congratulations}{total_money}")
        print("----------------------------")
        return{
            "statement":True
        }

def Q2(total_money):
    # global total_money
    q_index = 2-1
    start_index = 1
    end_index = 2+1
    print(questions[q_index]["Q2"])
    
    target_question = "Q2"
    for question in options:                         # Iterate through the root list and print the values for the specified options
     if target_question in question:                 # it checks if target question is inside the index tuple
        for option in question[target_question]:     # loop in the list(array) to get the tuple(object)
            for key, value in option.items():        # here iteration happens inside the tuple. 
                print(f'{key}. {value}')                         # first index key and second value
    input_ans = (input("Enter the answer in block letter: ")) 
    print("The asnwer provided is :",input_ans)
    if(input_ans != right_answers[q_index]["Q2"]):
        print(condolense)
        print(f"{last_money}{total_money}")
        return{
            "statement": False
        }
    else:
        total_amount = 0
        for i in range(start_index, end_index):
            key, value = next(iter(amount[i].items()))
            # Remove commas from the value and convert it to an integer
            value = int(value.replace(',', ''))
            total_amount += value
            total_money = total_amount
        
        print(correct_ans)
        print(f"{congratulations}{total_money}")
        print("-------------------------------")
        return{
            "statement":True
        }

def Q3():
    global total_money
    q_index = 3-1
    start_index = 1
    end_index = 3+1
    print(questions[q_index]["Q3"])
    
    target_question = "Q3"
    for question in options:                         # Iterate through the list and print the values for the specified options
     if target_question in question:
        for option in question[target_question]:
            for key, value in option.items():        # here iteration happens inside the tuple. 
                print(f'{key}. {value}')                         # first index key and second value
    input_ans = (input("Enter the answer in block letter: ")) 
    print("The asnwer provided is :",input_ans)
    if(input_ans != right_answers[q_index]["Q3"]):
        print(condolense)
        print(f"{last_money}{total_money}")   
        return{
            "statement": False
        }
    else:
        total_amount = 0
        for i in range(start_index, end_index):
            key, value = next(iter(amount[i].items()))
            # Remove commas from the value and convert it to an integer
            value = int(value.replace(',', ''))
            total_amount += value
            total_money = total_amount
        print(correct_ans)
        print(f"{congratulations}{total_money}")
        return{
            "statement":True
        }
     
def root_question():
    if(Q1()["statement"] == True):
        if(Q2(total_money)["statement"] == True):
            Q3()

root_question()


# def testing():
#     global total_money
#     print(total_money)
#     print(initial_money)
#     total_money = "alternating"
#     # initial_money = "alternating"
#     print("alternative amount",total_money)        
#     print("alternative initial_money amount",initial_money)        
# def testing2():
#     print("testing2",total_money)     
# testing()
# testing2()

