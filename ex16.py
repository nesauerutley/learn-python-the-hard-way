# imports the function or parameter argv from the module sys
from sys import argv

# passes the arguments script and filename to the command line
script, filename  = argv

# prints a string to the command line, calls the argument filename via raw format string
print "We're going to erase %r." % filename
# prints a string to the command line
print "If you don't want that, hit CTRL-C (^C)."
# prints a string to the command line
print "If you do want that, hit RETURN."

# prompts the user for input
raw_input("?")

# prints a string to the command line
print "Opening the file..."
# opens the file called by argument filename in write mode
target = open(filename, 'w')

# prints a string to the command line
print "Truncating the file. Goodbye!"
# erases the content of the opened file
target.truncate()

# prints a string to the command line
print "Now I'm going to ask you for three lines."

# prompts the user to input a string and assigns it to the variable line1
line1 = raw_input("line 1: ")
# prompts the user to input a string and assigns it to the variable line2
line2 = raw_input("line 2: ")
# prompts the user to input a string and assigns it to the variable line3
line3 = raw_input("line 3: ")

# prints a string to the command line
print "I'm going to write these to the file."

# writes the string called by variable line1 to the target file
target.write(line1)
# writes a line break to the target file
target.write("\n")
# writes the string called by variable line2 to the target file
target.write(line2)
# writes a line break to the target file
target.write("\n")
# writes the string called by variable line3 to the target file
target.write(line3)
# writes a line break to the target file
target.write("\n")

# prints a string to the command line
print "And finally, we close it."
# closes the target file
target.close()
