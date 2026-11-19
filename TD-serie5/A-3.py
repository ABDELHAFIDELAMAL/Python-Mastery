class Date:
    mois = [
        "janvier", "fevrier", "mars", "avril",
        "mai", "juin", "juillet",
        "aout", "septembre", "octobre",
        "novembre", "decembre"
    ]

    def __init__(self, jour, mois, annee):
        self.__jour = jour
        self.__mois = mois
        self.__annee = annee

    def getAnne(self):
        return self.__annee

    def afficher(self):
        moi = Date.mois[self.__mois - 1]
        date = str(self.__jour) + " " + moi + " " + str(self.__annee)
        return date

    def comparer(self , date1 ):
        if date1.getAnne() > self.getAnne():
            print("date " , self.afficher() , "est superieur")
        else :
            print("date " , date1.afficher() , "est superieur")
date = Date(20, 12, 2004)
date2 = Date(20, 12, 2007)

date.comparer(date2)
