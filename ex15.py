# imports the function or parameter argv from the module sys
from sys import argv

# passes the arguments script and filename to the command line
script, filename = argv

# assigns the content of a file to be entered by the user to the value txt
txt = open(filename)

# prints a string followed by the content argument of the argument filename to the command line
print "Here's your file %r:" % filename
# prints the context of the file assigned to the variable txt to the command line
print txt.read()

# prints a string to the command line
print "Type the filename again:"
# prompts the user for input and assigns the input to the variable file_again
file_again = raw_input("> ")

# opens the file provided by the user and assigns the content to the variable txt_again
txt_again = open(file_again)

# prints the content assigned to the variable txt_again to the command line
print txt_again.read()
