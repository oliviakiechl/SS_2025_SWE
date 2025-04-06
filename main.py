
class Sensor():
    """
    A sensor  class that represents a sensor!
    """
    #Konstruktor
    def __init__(self, id):
        self.id = id
        self.messwert = None
        self.messwerte = []
        self.__passwort = "123456"
    
    def measure(self, messwert):
       self.messwert = messwert
       self.messwerte.append(messwert)
    
    def calc_mean(self):
        self.mittelwert = sum(self.messwerte)/len(self.messwerte)
        return self.mittelwert

    def get_passwort(self, superpasswort):
        if superpasswort == "bier":
            return self.__passwort

    def set_passwort(self, superpasswort):
        if superpasswort == "bier":
            self.__passwort = neues_passwort
    def reset(self, passwort):
        if passwort == self.__passwort:
                print("Auf Werkeinstellungen")
                self.messwert = None
                self.messwert = []
        else:
                print("Falsches Passwort!")


if __name__ == "__main__":
    s1 = Sensor("123")
    print(s1.id)
    s1.measure(10)
    s1.measure(20)
    s1.measure(30)
    s1.calc_mean()
    print(s1.__dict__)
    das_passwort = s1.get_passwort("bier")
    print(das_passwort)
    s1.reset(das_passwort)

    s1.set_passwort("bier", "test")
    print(s1.get_passwort("bier"))

class HR_Sensor(Sensor):
     # hier gibt es gar keinen Konstruktor 
     def __init__(self, id, typ):
          #Nimm den Konstruktor von oben (Elternklasse)
          super().__init__(id)
          self.typ = typ

     def calc_hrv(self):
          print("Die HRV ist 60")

if __name__ == "__main__":
     s1 = Sensor("1234")
     print(s1.id)

     s2 = HR_Sensor("2345")
     print(s2.id)
     s2.calc_hrv()
     print(hello world)