# Recursive function means that the function calls itself during
# its execution. The programmer has to make sure the parameters passed 
# recursively are updated every time so that the execution of the
# recursive function ends sometimes

def rangeSum(number):
    # There has to be an ending condition inside the function when
    # it doesn't call itself anymore
    if number <= 0:
        return 0
    return number + rangeSum(number -1)

def rangeSum_loop(number):
    result = 0
    while number > 0:
        result += number
        number -= 1
    return result

number = 6

print("Rekursiivinen:", rangeSum(number))
print("Silmukka:", rangeSum_loop(number))

def infinite(n=0):
    print(n)
    infinite(n + 1)

# infinite()

def factorial(n): # from week 6 exercises
  if n < 0:
    return None
  elif n == 0 or n == 1:
    return 1

  result = 1
  while n > 1:
    result *= n
    n -= 1

  return result

def factorial_recursive(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)
print("Kertoma silmukalla:", factorial(number))
print("Kertoma rekursiviisesti:", factorial_recursive(number))