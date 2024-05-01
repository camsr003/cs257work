import flask
from flask import render_template
import psycopg2
import random

app = flask.Flask(__name__)

#
@app.route('/')
def welcome():
    return render_template("welcome.html")
    
@app.route('/random')
def random_sent():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="richardsonc",
        user="richardsonc",
        password="berry437lamp")
  
    cur = conn.cursor()

    names = ["Aaron",
      "Abel",
      "Abraham",
      "Achilles",
      "Adam",
      "Adran",
      "Ammar",
      "Amon",
      "Arthur",
      "Artminas",
      "Boyd",
      "Brad",
      "Brandon",
      "Chuck",
      "Cicero",
      "Cinnabar",
      "Claudius",
      "Clay",
      "Clement",
      "Clive",
      "Cody",
      "Cole",
      "Colt",
      "Connor",
      "Conrad",
      "Cornelius",
      "Cozen",
      "Creon",
      "Crona",
      "Crow",
      "Cygnet",
      "Cypress",
      "Cyrus",
      "Daedalus",
      "Dalinar",
      "Damien",
      "Devin",
      "Dex",
      "Diar",
      "Diego",
      "Dimitri",
      "Dinell",
      "Diomedes",
      "Dior",
      "Dominic",
      "Donovan",
      "Dove",
      "Dragon",
      "Esker",
      "Ethan",
      "Eula",
      "Evaine",
      "Ezekiel",
      "Fabian",
      "Fahim",
      "Falco",
      "Falcon",
      "Faris",
      "Faust",
      "Feldspar",
      "Felix",
      "Ferdinand",
      "Ferguson",
      "Fern",
      "Feste",
      "Fraser",
      "Frederick",
      "Fritz",
      "Gabbro",
      "Gabriel",
      "Gael",
      "Gaius",
      "Galahad",
      "Izzy",
      "Jack",
      "Jackdaw",
      "Jackie",
      "Jacob",
      "Jaleel",
      "Jalen",
      "Jamal",
      "James",
      "Jamie",
      "Jason",
      "Jasper",
      "Jay",
      "Leon",
      "Leonardo",
      "Levi",
      "Lewis",
      "Liam",
      "Link",
      "Lloyd",
      "Loam",
      "Logan",
      "Lotus",
      "Louie",
      "Lucas",
      "Lucius",
      "Paul",
      "Pax",
      "Payton",
      "Pebble",
      "Penn",
      "Percy",
      "Peter",
      "Philip",
      "Phoenix",
      "Phos",
      "Pigeon",
      "Python",
      "Quail",
      "Quake",
      "Quan",
      "Quantum",
      "Quartz",
      "Quentin",
      "Quince",
      "Quincy",
      "Quirrel",
      "Radovan",
      "Raheem",
      "Raigh",
      "Rain",
      "Raj",
      "Rajul",
      "Rama",
      "Sigurd",
      "Valentine",
      "Valerian",
      "Vergil",
      "Victor",
      "Vin",
      "Vincent",
      "Wormwood",
      "Wren",
      "Xavier",
      "Xavos",
      "Xiao",
      "Yakub",
      "Zora",
      "Zote"]
    adjs = ["Great",
            "Gallant",
            "Destroyer",
            "Huge",
            "Majestic",
            "Terrible",
            "Scholar of the Burning Blood",
            "Scaleless",
            "Lord of Cinder",
            "Perfect",
           "Imperfect",
            "King",
            "Cursed",
            "Blessed",
           "Mad",
           "Fell Omen",
           "Misbegotten",
           "Best",
           "Beautiful",
           "Tired",
           "Restless",
           "Mariner",
           "Terrible",
           "Interesting",
           "Thoughtful",
           "Omen",
           "Rare",
           "Difficult",
           "Last Great Mage",
           "Pirate",
           "Malevolent",
           "First",
           "Bug Eater",
           "Forgotten",
           "Invisible",
           "Lonesome",
           "Putrid",
           "Benevolent"]
    
    sql = "SELECT * FROM uscitypop;"
    
    randomchance = random.randint(0, 100)
    
    if randomchance > 10:
        ancient = False
    else:
        ancient = True
        if randomchance > 5:
            era = " BC"
        else:
            era = None
        
    if ancient:
        randomyear = random.randint(0, 1800)
        if era == " BC":
            randomyear = random.randint(0, 10000)
    else:
        randomyear = random.randint(1900, 2023)
        
    randomname = names[random.randint(0, len(names) - 1)]
    one_million = random.randint(0, 1000000)
    if one_million == 1:
        randomadj = "One in a Million, Greatest of All that Is"
    else:
        randomadj = adjs[random.randint(0, len(adjs) - 1)]
    
    cur.execute( sql  )

    row_list = cur.fetchall()
    randomcityindex = random.randint(0, len(row_list) - 1)
    randomcity = row_list[randomcityindex][0]
    state = row_list[randomcityindex][1]
    randomcolor = colors[random.randint(0, len(colors) - 1)]
    
    if ancient:
        randomsent = randomname + " the Ancient " + randomadj + " was born near modern day " + randomcity + ", " + state + " in the year " + str(randomyear)
        if era:
            randomsent = randomname + " the Ancient " + randomadj + " was born near modern day " + randomcity + ", " + state + " in the year " + str(randomyear) + era
    else:
        randomsent = randomname + " the " + randomadj + " was born in " + randomcity + ", " + state + " in the year " + str(randomyear)
    return render_template("randomsent.html", rand_sent = randomsent, rcolor = randomcolor)
        
if __name__ == '__main__':
    my_port = 5124
    app.run(host='0.0.0.0', port = my_port) 
