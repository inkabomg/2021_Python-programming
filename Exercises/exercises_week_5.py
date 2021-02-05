# Harjoitus 1:
# Suunnittele ja toteuta listan väärinpäin kääntävä algoritmi. Algoritmi toimii
# siis siten, että käännetyn listan ensimmäinen alkio on alkuperäisen listan
# viimeinen alkio jne. Älä käytä list.reverse() funktiota.

cars = ["Toyota", "Mazda", "Ford", "Audi"]
# print("Original list:", cars)

reversed_list = cars[::-1]
print("Reversed list:", reversed_list)

# OR

cars = ["Toyota", "Mazda", "Ford", "Audi"]
reversed = []
for index in range(len(cars)):
    reversed.append(cars[-1 * (index + 1)])
print(reversed)

# Harjoitus 2:
# Suunnittele ja kirjoita algoritmi, joka luo uuden sanan alkuperäisen sanan
# perusteella siten, että alkuperäisestä sanasta otetaan uuteen sanaan joka toinen kirjain.

word = "saippuakauppias"
# step through the string by 2s (which will return every other character)
print(word[::2])

# OR

word = "saippuakauppias"
index = 0
result = ""
while index < len(word):
    if index % 2 == 0:
        result += word[index]
    index += 1
print(result)


# Harjoitus 3:
# Laske montako parillista ja paritonta numeroa listassa (tai tuplessa) on.

numbers = (3, 1, 6, 3, 4, 7, 0, 6, 3, 2, 6, 8, 3)

even_count, odd_count = 0, 0

# iterating each number in tuple
for num in numbers:
    # checking condition
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers in the tuple:", even_count)
print("Odd numbers in the tuple:", odd_count)

# Harjoitus 4:
# Pyydä käyttäjää syöttämään sanoja, kunner käyttäjä syöttää sanan "stop".
# Lopuksi tulosta kaikki käyttäjän syöttämät sanat (paitsi "stop").

words = input("Enter a word: ")
allWords = "" 
while words != "stop":
    allWords = allWords + " " + words
    words = input("Enter a word: ")
print(allWords)

# Harjoitus 5:
# Pyydä käyttäjää syöttämään, monenko luvun keskiarvon tämä haluaa laskea.
# Tämän jälkeen pyydä käyttäjää syöttämään näin monta lukua. Laske
# lopuksi lukujen  keskiarvo ja tulosta tämä käyttäjälle.

num2 = int(input("How many numbers: "))
total_sum = 0

for n in range(num2):
    numbers = float(input("Enter a number: "))
    total_sum += numbers
avg = total_sum / num2
print("Average of the ", num2, " input numbers is: ", avg)

# Harjoitus 6:
# Pyydä käyttäjää syöttämään sana. Laske montako kertaa eri kirjaimet esiintyvät sanassa.
# Lopuksi tulosta kirjaimet ja niiden esiintymiskerrat. 
# Esimerkkitulosteet:
# Syötä sana > tietokone
# { "t": 2, "i": 1, "e": 2, "o": 1, "k": 1, "n": 1}
# Vihje: operaattorit in ja not in

import collections

word = input("Enter a word: ")
frequencies = collections.Counter(word)
repeated = {}

# iterate through frequencies dictionary
for key, value in frequencies.items():
    # if character repeats, add to repeated dictionary
    if value > 0:
        repeated[key] = value
print(repeated)