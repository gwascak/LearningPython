
# These are all of the variables. Each is defined with a value.
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# This print uses the 'cars' variable.
print "There are", cars, "cars available."
# This print uses the 'drivers' variable.
print "There are only", drivers, "drivers available."
# This print uses the 'cars_not_driven' variable.
print "There will be", cars_not_driven, "empty cars today."
# This print uses the 'carpool_capacity' variable.
print "We can transport", carpool_capacity, "people today."
# This print uses the 'passengers' variable.
print "We have", passengers, "to carpool today."
# This print uses the 'average_passengers_per_car' variable.
print "We need to put about", average_passengers_per_car, "in each car."
