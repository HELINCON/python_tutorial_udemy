splitString =  "This string has been\nsplit over\nseveral\nlines"
print(splitString)
tabbedstring = "1\t2\t3\t4\t5"
print(tabbedstring)


print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# in above code without slash(\) 'e 's  cannot be written as the entire sentence is in single quote string'


print("The pet shop owner said \"No, no, \'e\'s uh,...he's resting\".")
# in the above code "No and last double quote(") cannot be written as the entire sentence is in double quotes
# This is what we call escapechar.


print("""The pet shop owner said "No, no, 'e's uh, ... he's resting".""")
# As we have triple quotes in ending and starting so there is no need to escape any string quote("" or '')

anotherSplitString = """This string has been 
split over 
several 
lines"""
# this will give output downwards in console

print(anotherSplitString)
# another use of triple quotes

print("""This string has been \
split over \
several \
lines""")
# by using backslash if we escape the lines then the output will come in a single sentence in console

print("""The pet shop owner said "No, no, \
'e's uh, ... he's resting".""")

print("c:users\\timbu\\notes.txt")
print(r"c:users\timbu\notes,txt")
# in above both the cases though backward slash are there still to avoid escaping we used double slash or r in the string