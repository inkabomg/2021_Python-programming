'''
Harjoitus 1
Kirjoita rekursiivinen funktio, joka tulostaa Fibonaccin lukujonon n ensimmäistä termiä.
Fibonaccin lukujono muodostuu seuraavasti:
F(n) = 0, kun n = 0
F(n) = 1, kun n = 1
F(n) = F(n-1) + F(n-2), kun n > 1
Lähde: https://fi.wikipedia.org/wiki/Fibonaccin_lukujono

Ratkaisu voi olla helpompi, jos jaat sen useampaan funktioon.
'''
# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
# The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n - 2) + fibonacci(n - 1))

number = 10

# check if the number of terms is valid (positive integer, 1 and above)
if number <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(number):
       print(fibonacci(i), end = " ")

print()

'''
Harjoitus 2
Kirjoita funktio, joka laskee numeroiden määrän luvussa rekursiivisesti.
Esim. luvun 10253 tulos on 5 ja luvun 42 tulos on 2.
'''

def digit(n):
      if n < 10:
          return 1
      else:
          return 1 + digit(n/10)

print("Result:", digit(10253))

print()

'''
Harjoitus 3
Alla oleva funktio tarkistaa, onko sana palindromi. Kirjoita funktiosta rekursiivinen versio.
Ratkaisu voi olla helpompi, jos jaat sen useampaan funktioon.

def isPalindrome(word):
   word = word.lower()

   # Poistaa kaikki white spacet
   word = "".join(word.split())

   start = 0
   end = len(word) - 1

   while start <= end:
      if word[start] != word[end]:
         return False
      start += 1
      end -= 1
   return True
'''

def ispalindrome(word):
    word = word.lower()
    word = "".join(word.split())

    if len(word) < 2:
        return True 
    if word[0] != word[-1]:
        return False

    return ispalindrome(word[1:-1])

print(ispalindrome("tac o cat"))