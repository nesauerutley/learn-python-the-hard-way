# imports the function or parameter argv from the module sys
from sys import argv

# passes the arguments script, input_file to the command line
script, input_file = argv

# defines the function print_all
# pases the argument f
def print_all(f):
    # prints the content of the argument to the command line
    print f.read

# defines the function rewind
# passes the argument f
def rewind(f):
    # returns to the beginning to the content passed by the argument
    f.seek(0)

# defines the function print_a_line
# passes the arguments line_count, f
def print_a_line(line_count, f):
    # prints argument line_count to the command line
    # prints the content of the co-ordinating line
    print line_count, f.readline()

# assigns the content of input_file to the variable current_file
current_file = open(input_file)

# prints a string to the command line
print "First, let's print the whole file:\n"

# calls the function print_all
# passes the argument current_file
print_all(current_file)

# prints a string to the command line
print "Now let's rewind, kind of like a tape."

# calls the function rewind
# passes the argument current_file
rewind(current_file)

# prints a line to the command line
print "Let's print three lines:"

# sets the variable current_line to the integer value 1
current_line = 1
# calls the function print_a_line
# passes the arguments current_line, current_file
# this should print the first line
print_a_line(current_line,current_file)

# sets the variable current line to current_line + 1
current_line += current_line
# calls the function print_a_line
# passes the arguments current_line, current_file
# this should print the second line
print_a_line(current_line, current_file)

# sets the variable current line to current_line + 1
current_line += current_line
# calls the function print_a_line
# passes the arguments current_line, current_file
# this should print the third line
print_a_line(current_line, current_file)
