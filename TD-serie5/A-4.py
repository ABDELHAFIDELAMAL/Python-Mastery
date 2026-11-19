class Vecule:
    def __init__(self , poids , vitesse):
        self.poids = poids
        self.vitesse = vitesse

    def avance(self):
        return str(self.poids) + str(self.vitesse)


class Voiture(Vecule):
    def __init__(self , poids , vitesse , nombrePassagers):
        super().__init__(poids , vitesse)
        self.nombrePassagers = nombrePassagers

    def allume_autoradio(self):
        return str(self.poids) + " kg " +str(self.vitesse) + " Km/h " +str(self.nombrePassagers) + " Passagers"

bmw = Voiture(2300 , 350 , 4)
print(bmw.allume_autoradio())


