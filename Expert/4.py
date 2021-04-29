#Write a Python code to read an integer in a file e.g 123 and convert it to words e.g One hundred and twenty three and write the result back to the same file such that your file will have "123 One hundred and twenty three " in it
from num2words import num2words

file = open("test.txt","r")
integer = int(file.readline())
  
# Most common usage.
number_words = num2words(integer)
file.close()
file = open("test.txt","w")
file.writelines(str(integer) +"\t"+ number_words)
print(number_words)