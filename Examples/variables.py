# -merkin saa shift + comd + 7

# Muuttujien määrittäminen. Python tulkki osaa päätellä tyypin muuttujan arvosta
muuttuja1 = 1 #Integer
muuttuja2 = "Tekstiä" #String 

print(muuttuja1)

# Python on dynaamisesti tyypitetty kieli
# Muuttuja tyyppi päätellään ajon aikana, kun muutujan alustava rivi suoritetaan
# Muuttujan tyypin pystyy muuttamaan määrittämällä muuttujan uudelleen
muuttuja1 = "Tekstiä" # Muuttujan tyyppi muuttui integeristä stringiksi

print(muuttuja1)

muuttuja1 = 1 #Integer, kokonaisluku
muuttuja2 = "Tekstiä" #String, merkkijono
muuttuja3 = 1.2 #Float, desimaaliluku
muuttuja4 = True #Boolean, totuusarvo (True tai False) !! Iso alkukirjain, toisin kuin javascriptissä !!

numero1 = 2
numero2 = 4

tulos = 0

# Yhteenlasku
tulos = numero1 + numero2

print(tulos)

# Vähentää tulos-muuttujasta muuttujan numero1 arvon
# ja tallentaa tuloksen tulos-muuttujaan
# tulos = tulos - numero1 (pitkä versio)
tulos -= numero1

# Jakolasku
# Tulos float-tyyppiä, vaikka molemmat: jaettava ja jakaja ovat kokonaislukuja
tulos = numero1 / numero2
print(tulos)

# Jakolasku, joka tulostaa kokonaisluvun
tulos = numero1 // numero2
print(tulos)

# Vastaavasti:
# += lisäys ja sijoitus
# -= vähennys ja sijoitus
# *= kertolasku ja sijoitus
# /= jakolasku ja sijoitus
# //= kokonaislukujen jakolasku ja sijoitus

# Python on vahvasti tyypitetty kieli
muuttuja1 = 10
muuttuja2 = "Tekstiä"

# Esimerkiksi eri tyyppisten muuttujien lisäys ei ole mahdollista
# print(muuttuja2 + muuttuja1) # TypeError: can only concatenate str (not "int") to str

# Koodaajan vastuulla on suorittaa tyyppimuunnos
# Esim. alla oleva koodi muuttaa kokonaisluvun string:iksi, jonka jälkeen lisäys toimii
print(muuttuja2 + str(muuttuja1))

# Lainausmerkit
print("Tulostuuko tämä?")
print('Tämä on vastaava merkkijono')
print('Tämä on "lainaus"') # Lainausmerkkien käyttö merkkijonon sisällä
print("Tämä on \"lainaus\"") # Lainausmerkit voidaan merkitä kenoviivalla,
# jolloin se tulkitaan kuuluvan osaksi merkkijonoa.

# Pitkät tekstit pitää katkaista rivinvaihtomerkillä \, mikäli haluamme rivittää sen
# usealle riville (muuten Python tulkitsee koodirivin päättyneeksi)
print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud \
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure \
dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt \
ollit anim id est laborum.")

# """ määrittää usean rivin merkkijonon

longText = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(longText)

# Usean rivin kommenttina Pythonissa voidaan käyttää """ operaattoria
""" Tämä
on
usean
rivin
kommentti """

# Tyyppimuunnoksia:
# int(muuttuja) muuttaa muuttujan integeriksi
# float(muuttuja) muuttaa muuttujan desimaaliluvuksi
# str(muuttuja) muuttaa muuttujan stringiksi

print(bool(0)) # False
print(bool(1)) # True
print(bool(-1)) # True