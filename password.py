# By ahmad alassaf
[Author => theviperxxsy]
#! / usr / bin / env python
from  random  import choice
 
values =  "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
length =   raw_input ( "Enter the length you want the password to have:" )
length =  int  ( length )  #We convert the value length from string to int
 
p =  ""  #We declare the variable where we keep the password
p = p. join ( [ choice ( values )  for i in  range ( length ) ] )  #We give random values ??to each position of the array
print  ( "Your password is:" + p )  #We give the value of the resulting array
 