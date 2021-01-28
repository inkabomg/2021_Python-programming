phones = ("Nokia", "Apple", "Samsung")
print(phones)

phone = phones[1]
print(phone) # Prints "Apple"

# phones.append("OnePlus") does not work with tuple, instead:

phoneList = list(phones)
phoneList.append("OnePlus")
phones = tuple(phoneList)
print(phones)