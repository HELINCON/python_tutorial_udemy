
# hardcoded 4 questions with answers
 
def Q2():
      print('Next question is on the screen below')
      print('Q2. What is the national animal of India')
      print("A. Cow")
      print('B. Tiger')
      print('C. Hippopotamus')
      print('D. Dog')
      answer = input('Enter the correct option: ')
      if(answer != 'B'):
        print('Oops ! Wrong answer')
        print('Better Luck Next Time')
        return {
            'bool':False
        }
      else:
          print('Congratulations !')
          print('You have passed the next step and have won Ten Thousand rupees (Rs.10,000)')
          return {
              'bool':True
          }

def Q3():
      print('Next question is on the screen below')
      print('Q3. What is the national flower of India')
      print("A. Daisy")
      print('B. Jasmine')
      print('C. Mariegold')
      print('D. Lotus')
      answer = input('Enter the correct option: ')
      if(answer != 'D'):
        print('Oops ! Wrong answer')
        print('Better Luck Next Time')
        return {
            'bool':False
        }
      else:
          print('Congratulations !')
          print('You have passed the next step and have won Twenty Thousand rupees (Rs.20,000)')
          return {
            'bool':True
        }

def Q4():
      print('Next question is on the screen below')
      print('Q4. What is the national Tree of India')
      print("A. Banana")
      print('B. Banyan')
      print('C. Palm')
      print('D. Coconut')
      answer = input('Enter the correct option: ')
      if(answer != 'B'):
        print('Oops ! Wrong answer')
        print('Better Luck Next Time')
        return {
            'bool':False
        }
      else:
          print('Congratulations !')
          print('You have passed the next step and have won Fifty Thousand rupees (Rs.50,000)')
          return {
            'bool':True
        }
  
def Q1():
    print("Welcome to KBC")
    print("Q1. what is national bird of India ?")
    print("A. peacock")
    print("B. Pigeon")
    print("C. Crow")
    print("D. Owl")
    
    Answer = (input("Enter the correct option: "))
    if Answer != 'A':
        print('Oops ! Wrong answer')
        print('Better Luck Next Time')
        return {
            'bool':False
        }
    else:
        print("Congratulations !")
        print("You have passed the first stage")
        print("You have won Five Thousand Indian Rupees (Rs. 5000)")
        return {'bool': True}
         
def RootQuestion():
    if Q1()['bool'] == True:
        if Q2()['bool'] == True:
            if Q3()['bool'] == True:
                Q4()
    else:
        print("Something went wrong")
                
               
RootQuestion()

