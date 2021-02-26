# Hakee kuvat rekursiivisesti siitä kansiosta, jossa tämä skripti on ja
# kaikista sen kansion alikansioista.

# Moduulin köyttöönotto, os on Pytyhon sisäänrakennettu moduuli, jolle
# voidaan suorittaa erilaisia järjestelmään liittyviä toiminnallisuuksia.
import os

# dir: sen hakemiston tiedostopolku, josta kuvia haetaan
# pics: lista, johon löydettyjen kuvien tiedostopolut tallennetaan

def find_pics(dir, pics):
    # listdir palauttaa parametrina saadun kansion sisältämät tiedostot ja kansiot
    files = os.listdir(dir)
    for file in files:
        # Tiedoston absoluuttinen sijainti kovalevyllä
        path = os.path.join(dir, file)
        if os.path.isdir(path):
            # Tiedosto onkin kansio, etstiään kuvia sen sisältä
            find_pics(path, pics)
        else:
            # Onko tutkittava tiedosto kuva?
            filename = file.lower()
            if file.endswith(".png") or file.endswith(".jpg"):
                pics.append(path)

pics = []
# Tämän skriptin sisältävän kansion tiedostopolku
os.path.realpath(__file__)
# Haetaan kuvat
find_pics(current_dir, pics)

for pic in pics:
    print(pics)
