# HARJOITUS
# Kirjoita ohjelma, joka kysyy käyttäjän nimeä. Ohjelma tulostaa esim. tekstin
# "Mikä sinun nimesi on?" nimeä kysyttäessä.
# Jos nimi on kirjoitettu pienellä alkukirjaimella, ohjelma muuttaa nimen alkukirjaimen
# isolla kirjoitetuksi. Lopuksi ohjelma tulostaa "Sinun nimesi on <Nimi>"

# syote.capitalize() muuttaa vain ensimmäisen merkkijonon ensimmäisen kirjaimen isoksi.
# syote.title() muuttaa jokaisen merkkijonon...
print("Mikä sinun nimesi on?")
syote = input()
print("Sinun nimesi on " + syote.title())

# print("Mikä sinun nimesi on?")
# txt = input()
# x = txt.title()
# print("Sinun nimesi on " + (x))

name = input("What is your name? ")
print("Your name is " + name.title())