'''
Harjoitus 1
Kirjoita funktio, joka ottaa parametrina määrittämättömän määrän numeroita ja 
kertoo ne yhteen. Funktio palauttaa tuloksen paluuarvona.
'''

def multiply(*numbers):
    if len(numbers) == 0:
    # Early exit
        return 0
    
    result = 1
    for number in numbers:
        result *= number
    return result

num = multiply(9, 8, 7, 6, 5, 4)

print(num)

'''
Harjoitus 2
Kirjoita funktio, joka palauttaa suurimman luvun, mikä on tallennettu parametrina
saatuun tietorakenteeseen. Mieti myös sopiva arvo palautettavaksi siinä tapauksessa, että 
tietorakenne ei sisällä mitään lukuja.
Toteuta myös vastaava funktio, mikä palauttaa pienimmän luvun tietorakenteessa.
'''

def max(*numbers):
  maxValue = None
  for number in numbers:
    if maxValue == None or number > maxValue:
      maxValue = number
  return maxValue

number = max(44, 529, 11, 5, 73, 112, 99)
print("The largest value in collection:", number)

def min(*numbers):
  minValue = None
  for number in numbers:
    if minValue == None or number < minValue:
      minValue = number
  return minValue

'''
Harjoitus 3
Kirjoita funktio, joka laskee parametrina saadun sanan vokaalisen määrän. Vokaaleja
ovat kirjaimet [a, e, i, o, u, y, ä, ö] (ts. suomen kielen mukaiset character :)
Funktio palauttaa vokaaleiden määrän.
'''
# Count vowels using dictionary 
def checkVowels(word): 
    word = word.lower()
    vowels = 'aeiouyäö'
    result = 0
 
    for character in word: 
        if character in vowels: 
            result += 1    
    return result 

print (checkVowels('saippuakauppias')) 

# OR

def vowels(word):
    character = 0
    for i in word:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i == 'y' or i == 'ä' or i == 'ö'):
            character += 1
    return character

# Printing the number of vowels in total, not specifying which vowels.
print(vowels('koira'))

'''
Harjoitus 4
Kirjoita funktio, joka laskee parametrina välitetyn positiivisen kokonaisluvun
kertoman. Toteuta myös virheiden käsittely.
Määritelmä: "Positiivisen kokonaisluvun n kertoma on luvun n ja kaikkien sitä pienempien 
positiivisten kokonaislukujen tulo, ja se merkitään n!."
(Wikipedia, https://fi.wikipedia.org/wiki/Kertoma)
 
Nollan kertomaksi on sovittu 1.
'''
def factorial(number):
    factorial = 1

    if number == 0:
        print("The factorial is 1")
    elif number < 0:
        print("Factorial does not exist for negative numbers")
    else:
        for num in range(1, number + 1):
            factorial *= num
        print("The factorial is", factorial)

factorial(1)
factorial(6)
factorial(-1)

# OR (teachet's example)

def factorial(n):
  if n < 0:
    return None
  elif n == 0 or n == 1:
    return 1

  result = 1
  while n > 1:
    result *= n
    n -= 1

  return result

'''
Harjoitus 5
Palindromi
Kirjoita funktio, joka tarkistaa, onko sana palindromi. Palindromi on sana, joka on sama
kirjoitettuna oikein ja väärin päin. Sanan kirjainten koolla ei ole merkitystä.
Oletus: Sana ei sisällä white space -merkkejä (rivinvaihto, välilyönti, tabulaattori).
Bonus: Sana saa sisältää white space -merkkejä, mutta niitä ei oteta huomioon tarkistettaessa,
onko sana palindromi.
'''

def palindromi(word):
  word = word.lower()

  word = "".join(word.split())
  
  start = 0
  end = len(word) - 1

  while start < end:
    startChar = word[start]
    endChar = word[end]

    if startChar != endChar:
      return False

    start += 1
    end -= 1

  return True


print(palindromi("taco cat"))