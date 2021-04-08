# Yksikkömuunnin
#
# Kirjoita sovellus yksikkömuunnosten tekemiseen.
# Ohjelman tulee kysyä käyttäjältä, millaisen yksikkömuunnoksen tämä haluaa tehdä.
# Vaihtoehtoja esimerkiksi:
# t: Lämpötilamuunnos
# v: Valuuttamuunnos
#
# Kun käyttäjä on valinnut haluamansa muunnoksen: kysy käyttäjältä lisätietoja muunnoksesta
# Esim.
# Lämpötilamuunnos:
# 1: Celcius -> Fahrenheit
# 2: Fahrenheit -> Celcius
#
# Tämän valinnan jälkeen kysy käyttäjältä muunnettava arvo
# Esim:
# Anna lämpötila
#
# Lopuksi ohjelma tulostaa muunnoksen tiedot
# Esimerkkiajo (englanniksi, saa toteuttaa myös suomeksi):
# > t
# Convert temperature
# 1: Celcius to Fahrenheit
# 2: Fahrenheit to Celcius
# > 1
# Temperature to convert
# > 20
# 20°C = 68.0°F
# >
#
# Tehtävässä saatte valmiina Conversion-luokan. Peri tästä luokasta muunnoksissa
# tarvittavat luokat. Esimerkki lämpötilalle
# class TemperatureConversion(Conversion)
# Tämä luokka muuntaa lämpötiloja °C ja °F välillä
# convert-funktio muuntaa esim. °C -> °F ja
# convertBack °F -> °C
#
# Tehtävänanto:
# Toteuta ylläkuvattu toiminnallisuus ja tee tuki lämpötilamuunnoksille (°C -> °F ja °F -> °C).
# Lisäominaisuutena voit toteuttaa valuuttamuunnoksia (tuki €, $ ja £)
# Valuuttamuunnokset näiden valuuttojen välillä vaatii siis kolmen luokan toteuttamista,
# muunnokset € ja £ välillä, muunnokset £ ja $ välillä ja muunnokset $ ja € välillä.
#
# Palauta toteuksesi Samille ensi torstaihin klo 12 mennessä osoitteeseen sami.kojo@tuni.fi
# zip-pakattuna tiedostona (koulun sähköposti ei salli .py-tiedostojen lähettämistä).


class Conversion:
  def __init__(self, value):
    self.value = value
    self.source = ""  # Lähdeyksikkö, esim. €
    self.destination = ""  # Kohdeyksikkö, esim. $

class TemperatureConversion(Conversion):
  def __init__(self, value):
    super().__init__(value)
    self.source = "°C"
    self.destination = "°F"

  def convert(self):
    return self.value * (9 / 5) + 32

  def convertBack(self):
    return (self.value - 32) * (5 / 9)

def main():
    print("Choose which unit converter to use:", "t: temperature", "c: currency", sep="\n")
    command = input("> ").strip().lower()
    if command == "c":
        print("The currency converter isn't available yet")
    elif command == "t":
        convertTemperature()


def convertTemperature():
  conversion = 0

  while conversion != 1 and conversion != 2:
    print("1: Celcius -> Fahrenheit", "2: Fahrenheit -> Celcius", sep="\n")
    try:
      conversion = int(input("= "))
    except ValueError:
      conversion = 0

  value = None
  while value == None:
    print("Syötä muunnettava lämpötila")
    try:
      value = float(input("> "))
    except ValueError:
      value = None

  converter = TemperatureConversion(value)

  if conversion == 1:
    source = converter.source
    destination = converter.destination
    convertedValue = converter.convert()
  else:
    source = converter.destination
    destination = converter.source
    convertedValue = converter.convertBack()

  print(f"{value}{source} = {convertedValue}{destination}")


if __name__ == "__main__":
  main()