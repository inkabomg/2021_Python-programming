#!/usr/bin/python3

import cgi
import cgitb
import os
import json
from os import path
import Highscore.config # Pakko myöntää että en tiedä miten tää olis pitänyt importtaa oikein, yritys oli kuitenkin kova

filePath = "/home/ssinla/cgi-data/scores.csv"

# Poista tämä rivi, kun sovellus on valmis. Tuotantokäytössä emme halua koskaan paljastaa koodissa
# potentiaalisesti olevia bugeja.
# cgitb.enable()

# Luokan (tiko3) kanssa muutamaan kertaan pohdittu yhdessä, ja koitettu auttaa toisiamme. Käytin itsekin highscore-luokkaa,
# ja erinäisiä funktioita, jotka hyödyntävät toisiaan. "updateScores"-funktioon kysyin suoraa apua, enkä täysin ymmärrä
# miksi käytössä tuple (sekä enumerate-toiminto vielä epäselvä..). Osa täysin omaa koodia, osaan saanut apua/täytettä
# luokkalaisilta (mm. Rosanne, Jasmin, Hilla H., Samuli).

def add(name, score):

    data.update({"name" : name})
    data.update({"score" : score})

  # TODO: lisää tiedostoon. Listassa max 10 kohtaa, jos listalle lisätään
  # uusi, sen täytyy korvata yksi (alin score poistuu)

class highscore:
  def __init__(self, path):
    self.readFile()
    self.scores = {}
    self.firstList = []
    self.finalDict = {}
    self.jsonData = {}

    self.filePath = path # .csv tiedostolle

  # Open the file
  def readFile(self):
    with open(self.filePath) as file: # 'r'
      # Go through the file line by line
      for row in file:
        (name, score) = row.split(";") # Tietojen erotusmerkkinä käytin ;
        self.scores[name] = int(score) # Score täytyy olla int-muodossa, ei str
  
  # Arrange in descending order (highest score at the top)
  def sortScores(self):
    self.firstList = sorted(self.scores.items(), key= lambda i: i[1], reverse = True) # Tämä litanja löytyi suoraan Googlesta, en tiedä ajaako homman oikein..
    return self.firstList

  # The original list doesn't have the places (from 1 to 10), adding them
  # [index] starts from zero, so putting 0-9
  def sortedDict(self):
    self.firstList()
    self.finalDict = {1: self.firstList[0], 2: self.firstList[1], 3: self.firstList[2], 4: self.firstList[3], 5:self.firstList[4], 6:self.firstList[5], 7: self.firstList[6], 8: self.firstList[7], 9: self.firstList[8], 10: self.firstList[9]}
    return self.finalDict # Lopullinen, järjestelty dictionary
  
  def updateScores(self):
    self.newScores = ""
    self.sortScores()
    for index, tuple in enumerate(self.firstList):
      name = tuple[0]
      score = tuple[1]
      self.newScores += " " + int(score) + "\n"

    # If an error occurs, prints "Error"
    try:
      file = open(self.filePath, "w", encoding="utf-8")
      file.write(self.newScore)
    except:
      print("Error! Unable to write to the file")
    finally: # "finally" will be executed regardless if the try block raises an error or not
      # Always close opened file once you're done with it
      file.close()

  # Shown as JSON-form 
  def run(self):
    self.sortedDict()
    jsonData = json.dumps(self.finalDict, indent=4) # indent = 4, jotta näyttää kivemmalta
    return(jsonData)


# Points are sent to the application in JSON format.
print("Content-type: application/json\n\n")

# Clarification of the HTTP-method
cgi_method = os.environ["REQUEST_METHOD"]
if cgi_method == "POST":

  # Reading the parameters
  data = cgi.FieldStorage()
  name = data.getvalue("name", "")
  score = int(data.getvalue("score", "")) # MUISTA INT !!!!!!
  user = data.getvalue("user", "")
  password = data.getvalue("password", "")

  # Points can be added successfully when the correct IDs have been entered
  if (Highscore.config.verify_password(user, password)) == True:
    # TODO: minne haluat lisätä .add(name, score)
    print("Function was successful")
  else:
    print("Wrong username and/or password")

else:
  print(highscore.run())