a = 20
b = 20

# Equals: a == b
# Not equals: a != b

if a == b:  # Is a equal to b?
    print(a, "equals", b)
else:
    # with sep-parameter we can define the separator of print-function
    print(a, "does not equal", b)

if a != b:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)

if not a == b:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)

# Less than: a < b
# Greater than: a > b

if a < b:
    print(a, "is less than", b)
elif a > b:
    print(a, "is greater than", b)
else:
    print(a, "equals", b)

# Less than or equal to: a <= b
# Greater than or equal to: a >= b

if a <= b:
    print(a, "is less than or equals", b)
else:
    print(a, "is greater than", b)


result = a == b
print(result) # True, because both a and b are 20

if result:
    print(a, "equals", b)
else:
    print(a, "does not equal", b)

if not result:
    print(a, "does not equal", b)
else:
    print(a, "equals", b)


    