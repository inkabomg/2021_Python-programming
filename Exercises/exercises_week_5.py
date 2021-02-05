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

# Harjoitus 4:
# Pyydä käyttäjää syöttämään sanoja, kunner käyttäjä syöttää sanan "stop".
# Lopuksi tulosta kaikki käyttäjän syöttämät sanat (paitsi "stop").


# Harjoitus 5:
# Pyydä käyttäjää syöttämään, monenko luvun keskiarvon tämä haluaa laskea.
# Tämän jälkeen pyydä käyttäjää syöttämään näin monta lukua. Laske
# lopuksi lukujen  keskiarvo ja tulosta tämä käyttäjälle.

# Harjoitus 6:
# Pyydä käyttäjää syöttämään sana. Laske montako kertaa eri kirjaimet esiintyvät sanassa.
# Lopuksi tulosta kirjaimet ja niiden esiintymiskerrat. 
# Esimerkkitulosteet:
# Syötä sana > tietokone
# { "t": 2, "i": 1, "e": 2, "o": 1, "k": 1, "n": 1}
# Vihje: operaattorit in ja not in
