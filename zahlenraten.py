# Zahlenraten

import random

titel = "Willkommen beim Zahlen-Rate-Spiel!"
print (titel)
anfang = int(input("Bitte die Anfangs Zufallszahl eingeben"))
ende = int(input("Bitte die Ende Zufallszahl eingeben"))

zufallszahl = (random.randint(anfang,ende))
text = "Bitte versuche meine Zahl zwischen", anfang," und" ,ende , "zu erraten"
eingabeText = "Bitte gib eine Zahl ein: "
print (text)
fertig = False
anzahlDerVersuche = 0
while fertig == False:
    zahl = int(input(eingabeText))
    anzahlDerVersuche = anzahlDerVersuche + 1

    if (zahl == zufallszahl):
        print("gewonnen!")
        fertig = True
    elif(zahl < zufallszahl):
        print("die gesuchte Zahl ist größer")

    else:
       print("die gesuchte Zahl ist kleiner")

print("super, du hast dafür nur ", anzahlDerVersuche, "Versuche benötigt")
print("ende")
