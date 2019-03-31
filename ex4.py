# assigns the number 100 to the variable cars
cars = 100
# assigns the number 4 to the variable space_in_a_car
space_in_a_car = 4
# assigns the number 30 to the variable drivers
drivers = 30
# assigns the number 90 to the variable passengers
passengers = 90
# assigns the result of variable cars (100) minus variable drivers (30) to the variable cars_not_driven
# cars_not_driven = 70
cars_not_driven = cars - drivers
# assigns the variable drivers (30) to the variable cars_driven
# cars_driven = 30
cars_driven = drivers
# assigns the result of variable cars_driven(drivers (30)) multiplied by variable space_in_a_car (4) to the variable carpool capacity
# carpool_capacity = 120
carpool_capacity = cars_driven * space_in_a_car
# assigns the variable average_passengers_per_car to the result of variable passengers (90) divided by variable cars_driven(drivers (30))
# average_passengers_per_car = 3
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."

print cars / drivers
print cars % drivers

print "Hey %s there." % "you"
