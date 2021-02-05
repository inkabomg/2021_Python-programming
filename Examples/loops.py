counter = 10

while counter >= 0:
    print(counter)
    counter -= 1
    # counter = counter - 1
else:
    # else condition runs after the loop's been successfully executed
    print("Loop ends")

# break and continue
# break interrupts the loop

counter = 10
index = 0
while counter >= 0:
    if index >= 5:
        break

    index += 1
    print(counter)
    counter -= 1
else:
    # break interrupts the loop, so else won't be executed
    print("Loop ends")

# continue statement stops the current iteration, and continues with the next
start = 0
end = 10

print("\n\n")
while start <= end:
    start += 1
    if start % 2 != 0: # %-modulo, divider
        continue
    print(start)

cars = ["Toyota", "Mazda", "Ford", "Audi"]

print("\n")

for car in cars:
    print(car)

print("\n")

sequence = range(len(cars))
for index in sequence:
    print(cars[index])

print("\n")


