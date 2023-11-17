a = "charlie"
b = a.upper()
print(b)
print(a)
a= "helincon"
print(a)


name = "charlie"
print("replaced name:",name.replace("charlie", "m x helincon")) # this replaces the value of the given variable

new_key = "This is for testing. wishing for best"
print(new_key.capitalize())

# **********************************************************************************************
text = "Quisquam non dolor amet ut magnam voluptatem ut. tempora sit quaerat ipsum. quiquia adipisci adipisci dolorem dolore. Sed adipisci ut eius est sed neque. Amet tempora amet aliquam voluptatem neque. Ut voluptatem ipsum eius aliquam. Quiquia ut quaerat aliquam neque. Etincidunt non eius etincidunt. Neque sed quisquam dolorem dolor non."

# Split the text into sentences based on the period (.)
sentences = text.split('. ')

# Capitalize the first letter of each sentence
capitalized_sentences = [kadali.capitalize() for kadali in sentences]
# here kadali is a temporary word used to denote each sentence fro mthe value of text 

# Join the sentences back together
result = '. '.join(capitalized_sentences)

print("result:",result)

# ********************************************************
from lorem.text import TextLorem

Lorem = TextLorem()

# Generate a dummy paragraph
dummy_paragraph = Lorem.paragraph()

split_sentence = dummy_paragraph.split(". ")
capitalize_it = [each_sentence.capitalize() for each_sentence in split_sentence]
escape_charactered_final_result = '.\n'.join(capitalize_it)
final_result  = '. '.join(capitalize_it)

print("final_result==>:",final_result)
print("escape_charactered_final_result==>:",escape_charactered_final_result)


# *************************************testing******************

from lorem.text import TextLorem

Lorem = TextLorem()

# Generate a dummy paragraph
new_dummy_paragraph = Lorem.paragraph()
print("new_dummy_paragraph===>",new_dummy_paragraph)
split_data = dummy_paragraph.split('. ')
capitalized_new_sentence = [each_line.capitalize() for each_line in split_data]

final_data = '.\n'.join(capitalized_new_sentence)
print("final_data receeived======>:", final_data)

# ********************************************************************
tst_text = "my name is frankok charlie"
found = tst_text.find("name") ## this will find the index if "name" is there but if it is not there it will not throw any error
 
found1 = tst_text.index("nanas") ## this will also find the index number of the given input 
print(found)
                            # but if the input is not there then it will throw specific error.

print(found1)