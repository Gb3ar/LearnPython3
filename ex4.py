cars = 100
space_in_a_car = 8.0
drivers = 40
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capasity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
cars_needed = passengers / space_in_a_car

print("There are", cars, "cars avaliable.")
print("There are only", drivers, "drivers avaliable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capasity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
print("We only need ", cars_needed,"to carpool toady.")

