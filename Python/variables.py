cars = 100
spaceinacar = 4.0
drivers = 30
passengers = 90
carsnotdriven = cars - drivers
carsdriven = drivers
fleetcapacity = carsdriven * spaceinacar
passengerspercar = passengers / carsdriven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", carsnotdriven, "empty cars today."
print "We can transport", fleetcapacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", passengerspercar, "in each car."
