# defines function cheese_and_crackers
# assigns two arguments: cheese_count, boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints a string to the command line containing the argument cheese_count
    print "You have %d cheeses!" % cheese_count
    # prints a string to the command line containing the argument boxes_of_crackers
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # prints a string to the command line
    print "Man that's enough for a party!"
    # prints a string to the command line
    print "Get a blanket.\n"

# prints a string to the command line
print "We can just give the function numbers directly"
# calls the function cheese_and_crackers
# passes the values 20, 30 for the arguments cheese_count, boxes_of_crackers
cheese_and_crackers(20,30)

# prints a string to the command line
print "OR, we can use variables from our script:"
# assigns the integer 10 to the value amount_of_cheese
amount_of_cheese = 10
# assigns the integer 50 to the value amount_of_crackers
amount_of_crackers = 50

# calls the function cheese_and_crackers
# passes the variables amount_of_cheese, amount_of_crackers for the arguments cheese_count, boxes_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints a string to the command line
print "We can even do math inside too:"
# calls the function cheese_and_crackers
# passes the sums of 10+20, 5+6 for the arguments cheese_count, boxes_of_crackers
cheese_and_crackers(10+20, 5+6)

# prints a string to the command line
print "And we can combine the two, variables and math:"
# calls the function cheese_and_crackers
# passes the sums of the integer assigned to the variable amount_of_cheese + 100 and the integer assigned to the variable amount_of_crackers + 1000 to the arguments cheese_count, boxes_of_crackers 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
