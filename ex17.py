# imports the function or parameter argv from the module sys
from sys import argv
# imports the function or parameter exists from the module os.path
from os.path import exists

# passes the arguments script, from_file, to_file to the command line
script, from_file, to_file = argv

# prints a string with two format variables to the command line
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
# in_file = open(from_file)
# indata = in_file.read()
# edited version: assigns the content from from_file to the variable indata
indata = open(from_file).read()

#prints a string to the command line that calls the format integer for the length of the content called by variable indata
print "The input file is %d bytes long" % len(indata)

# prints a format boolean to the command line
print "Does the output file exist? %r" % exists(to_file)
# prints a string to the command line
print "Ready, hit RETURN to continue, CTRL-C to abort."
# prompts the user for input
raw_input()

# assigns the variable out_file to the open argument to_file in write mode
# out_file = open(to_file, 'w')
# writes the content of variable indata to the variable out_file
# out_file.write(indata)
# edited version: opens the file linked by the argument to_file in write mode, writes the content of indata to it
open(to_file, 'w').write(indata)

# prints a string to the command line
print "Alright, all done."

# out_file.close()
# in_file.close()
