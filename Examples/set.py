# Set is defined with curly brackets {}
# You can't access items by indexing them

units = {"tank", "plane", "ship", "dog"}
print(units)

# Set is unordered and unindexed data collection
# -> the order of elements changes (also when adding or removing)

# New element is added to the data collection, not in order
units.add("soldier")
print(units)

# Multiple elements can be added at once (see [] in between ())
units.update(["heavy tank", "helicopter"])
print(units)

# Add-function has no effect if the element is already present
units.add("dog")
print(units)

unitList = ["tank", "plane", "ship", "dog", "dog", "dog"]
print(unitList)
unitSet = set(unitList) # Change list to set, to get rid of duplicates
print(unitSet)

# Discard and remove functions delete the element from data collection.
# The difference between these functions is that if the element is not
# in the set, discard does nothing, but remove raises a KeyError.
units.discard("dog")
print(units)

# units.remove("dog")
# print(units)

# Pop function works with set. Removes and returns
# an arbitrary set element. Raises KeyError if the set is empty.
random = units.pop()
print(random)

print(units)