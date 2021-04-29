#Get a list of name as an input from the user and make the first letters in caps and print each word as a list
from camelcase import CamelCase

def capitalize_word(word):
    c = CamelCase()
    return c.hump(word)
    
number_of_inputs = input('Enter number of names you want to enter : ')

input_names = []
for n in range(int(number_of_inputs)):
    input_names.append(input('Enter name '+str(n+1)+': '))

capitalised_words = map(capitalize_word,input_names)
print('Capitalised words are : ')
print(list(capitalised_words))
