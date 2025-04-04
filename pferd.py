# Klassen Definition

class Pferd2():

    #Konstruktor
    def __init__(self, mein_name, meine_groesse):
        print("Hier wird ein Pferd geboren!")
        print("Das Pferd ist", meine_groesse)
    
        #Das erste Attribut hinzufügen
        self.groesse = meine_groesse
        self.name = mein_name
        self.geschwindigkeit = "0 km/h"

    def sich_vorstellen(self):
        print("Ich bin", self.name, "und bin", self.groesse, "groß!")

    def laufen(self, geschwindigkeit):
        self.geschwindigkeit = geschwindigkeit 
        print("ich laufe mit", self.geschwindigkeit)

    #Instanzierung eines Objektes


    #Self müssen wir nie übergeben!
    
    pf1 = Pferd2("Beauty", "1,70m")
    pf2 = Pferd2("Black", "2,20m")

    pf1.sich_vorstellen()
    pf2.sich_vorstellen()

    pf1.laufen("30 km/h")
    print(pf1.geschwindigkeit)
    #print(pf1.groesse)
    #print(pf2.groesse)

    #print(pf1.name, "ist", pf1.groesse)
    #print(pf2.name, "ist", pf2.groesse)