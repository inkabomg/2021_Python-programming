# An unordered, changeable and indexed collection
# Contains key-value pairs. Keys are personalized.
# Defined by curly brackets {}

carInfo = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2010,
    "price": 6502.15
}

print(carInfo)

# Adding a key-value pair
carInfo["color"] = "red"
print(carInfo)

# Changing key's value
carInfo["year"] = 2011
print(carInfo)

# Storing data in a variable
price = carInfo["price"]
print(price)

# Removing specified key and return the corresponding value.
color = carInfo.pop("color")
print(color)

color = carInfo.pop("color", "N/A")
print(color)

print(carInfo)