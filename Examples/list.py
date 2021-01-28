# List items don't have to be the same type (not recommended though)
# Indexing starts from 0

#          0         1        2      3
cars = ["Toyota", "Mazda", "Ford", "Audi"]

print(cars)

# cars[-1] prints the last item, "Audi"
# cars[1:3] prints cars between 1 and 3 (3 not included), "Mazda", "Ford"


# Items can be added and removed

cars.append("Jeep") # append adds item to list (at the end of the list)
print(cars)

cars.insert(2, "Fiat") # Insert adds item
print(cars)

deleted = cars.pop() # Pop deletes item from list. If index hasn't been input,
#it deleted the last item on the list, "Jeep"
print(deleted)

deleted = cars.pop(1) # Deletes "Mazda"
print(deleted)

del cars[1:3] # deletes cars between 1 and 3 (3 not included), "Fiat", "Ford"
print(cars)

# del cars : deletes whole list, prints error
cars.clear() # Clear removes all items from list, but does not delete list
print(cars)