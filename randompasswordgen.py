#importing random method for generating random methods
#importing String method for ascii_letters,digits,punctuation symbols.
import random
import string
#Taking input from User
length=int(input("Enter Your Password Length:"))
#Adding Ascii_values,Digits,Punctuation Symbols to a variable.
char=string.ascii_letters
char+=string.digits
char+=string.punctuation
#generating password characters by using random method.
password="".join([random.choice(char) for i in range(length)])
#printing password for user defined length.
print("Your random Password is:",password)
