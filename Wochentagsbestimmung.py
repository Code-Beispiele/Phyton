import math
import time
from tkinter import *
LT = time.localtime()

# DAS FOLGENDE PROGRAMM WURDE VON @CODE-BEISPIELE GESCHRIEBEN:
# www.github.com/CODE-BEISPIELE
# BITTE NUR MIT ANGABE DEN QUELLCODE ANGEBEN.

# FEHLER:
# 223: Das angegebene Jahr liegt unter 0.
# 188: Die Ziffern des Datums sind zu lang/kurz.
# 189: Ein falscher Wert wurde bei der Auswertung entdeckt. Das Programm stoppt.

inputvar = input("Bitte Datum nach dem Muster TT.MM.JJJJ eingeben: ")
#                                             0123456789
if inputvar[0] == "0":
  d = int(inputvar[1])
else:
  d = int(inputvar[0] + inputvar[1])
if inputvar[3] == "0":
  m = int(inputvar[3])
else:
  m = int(inputvar[3] + inputvar[4])
# Bitte warten
print("Bitte warten...")
# Monatsberechnung
if m == 1:
  m = 11
elif m == 2:
  m = 12
elif m == 3:
  m = 1
elif m == 4:
  m = 2
elif m == 5:
  m = 3
elif m == 6:
  m = 4
elif m == 7:
  m = 5
elif m == 8:
  m = 6
elif m == 9:
  m = 7
elif m == 10:
  m = 8
elif m == 11:
  m = 9
elif m == 12:
  m = 10
# y wird ausgerechnet
if inputvar[8] == "0":
  y = int(inputvar[9])
else:
  y = int(inputvar[8] + inputvar[9])
if inputvar[6] == "0":
  c = int(inputvar[7]) 
else:
  c = int(inputvar[6] + inputvar[7])
if m == 11 or 12:
  if y == 0 and c == 21:
    c = 20
    y = 99
  elif y == 0 and c == 20:
    c = 19
    y = 99
  elif y == 0 and c == 19:
    c = 18
    y = 99
  elif y == 0 and c == 18:
    c = 17
    y = 99
  elif y == 0 and c == 17:
    c = 16
    y = 99
  elif y == 0 and c == 16:
    c = 15
    y = 99
  elif y == 0 and c == 15:
    c = 14
    y = 99
  elif y == 0 and c == 14:
    c = 13
    y = 99
  elif y == 0 and c == 13:
    c = 12
    y = 99
  elif y == 0 and c == 12:
    c = 11
    y = 99
  elif y == 0 and c == 11:
    c = 10
    y = 99
  elif y == 0 and c == 10:
    c = 9
    y = 99
  elif y == 0 and c == 9:
    c = 8
    y = 99
  elif y == 0 and c == 8:
    c = 7
    y = 99
  elif y == 0 and c == 7:
    c = 6
    y = 99
  elif y == 0 and c == 6:
    c = 5
    y = 99
  elif y == 0 and c == 5:
    c = 4
    y = 99
  elif y == 0 and c == 4:
    c = 3
    y = 99
  elif y == 0 and c == 3:
    c = 2
    y = 99
  elif y == 0 and c == 2:
    c = 1
    y = 99
  elif y == 0 and c == 1:
    c = 0
    y = 99
# Hier kann man den Entwicklermodus mit der Eingabe "1" anschalten.
Entwicklermod = input("Enwickler Modus an? ")
if Entwicklermod == "1":
    EMOD = 1
    print("[INFO]Der Entwicklermodus wurde aktiviert.")
else:
    EMOD = 0
cc1 = d + math.floor(2.6*m-0.2)
if EMOD == 1:
    print("Berechne d + math.floor(2.6*m-0.2)")
    print(cc1)
    time.sleep(1)
else:
    print("")
cc2 = cc1+y+math.floor(y/4)
if EMOD == 1:
    print("Berechne cc1+y+math.floor(y/4)")
    print(cc2)
    time.sleep(1)
else:
    print("")

cc3 = cc2+math.floor(c/4) - 2*c
if EMOD == 1:
    print("Berechne cc2+math.floor(c/4) - 2*c")
    print(cc3)
    time.sleep(1)
else:
    print("")

w = (cc3) % 7
if EMOD == 1:
    print("Fertig")
    print(w)
else:
    print("")
if EMOD ==1:
    print("Werte Ergebnis aus")
else:
    print("Fertig!")

if w == 0:
    print("Der Tag ist ein Sonntag")
elif w == 1:
        print("Der Tag ist ein Montag")
elif w == 2:
        print("Der Tag ist ein Dienstag")
elif w == 3:
        print("Der Tag ist ein Mittwoch")
elif w == 4:
        print("Der Tag ist ein Donnerstag")
elif w == 5:
        print("Der Tag ist ein Freitag")
elif w == 6:
        print("Der Tag ist ein Samstag")
else:
  print("Ein Fehler ist aufgetreten (Fehlernummer: 189)")

print("")
