from sys import argv

script, user_name, favorite_drink = argv
something_else_entirely = 'answer:'

print "Hi %s, I'm the %s script and I like %s too." % (user_name, script, favorite_drink),
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(something_else_entirely)

print "Where do you live %s?" % user_name
lives = raw_input(something_else_entirely)

print "What kind of computer do you have?"
computer = raw_input(something_else_entirely)

print '''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
''' % (likes, lives, computer)
