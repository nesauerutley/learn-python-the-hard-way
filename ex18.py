# this one is like your scripts with argv
# defines function and passes undefined number of arguments
def print_two(*args):
    # defines two variables as arguments
    arg1, arg2 = args
    # prints a string to the command line that calls two arguments
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
# defines function and passes in two arguments
def print_two_again(arg1, arg2):
    # prints a string to the command line that calls two arguments
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
# defines function and passes in one argument
def print_one(arg1):
    # prints a string to the command line that calls the argument
    print "arg1: %r" % arg1

# this one takes no arguments
# defines function and passes no arguments
def print_none():
    # prints a string to the command line
    print "I got nothin'."

# calls the function and assigns two strings to the argument values
# this will print a string containing the two values to the command line
print_two("Zed","Shaw")
# calls the function and assigns two strings to the argument values
# this will print a string containing the two values to the command line
print_two_again("Zed","Shaw")
# calls the function and assigns a string to the argument
# this will print a string containing the value to the command line
print_one("First!")
# calls the function, passes no arguments
# this will print a string to the command line
print_none()
