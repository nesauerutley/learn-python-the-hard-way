name = 'Naomi E. Sauer-Utley'
age = 30 # not a lie
height = (5 * 12 + 10) # inches
height_cm = round(height * 2.54)
weight = 122 # lbs
weight_kilos = round(weight /  2.205)
eyes = 'Green'
teeth = 'White'
hair = 'Mousy'

print "Let's talk about %s." % name
print "They're %d inches tall and %d cm tall." % (height, height_cm)
print "They're %d pounds and %d kilos heavy." % (weight, weight_kilos)
print "They've got %s eyes and %s hair." % (eyes, hair)
print "Their teeth are usually %s depending on the coffee" % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
