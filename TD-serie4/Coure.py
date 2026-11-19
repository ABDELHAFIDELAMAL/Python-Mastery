class Rectangle:
    def __init__(self, largeur , langeur ):
        self.langeur = langeur
        self.largeur = largeur

    def surface(self):
        return self.langeur * self.largeur

    def perimeter(self):
        return 2 * (self.langeur + self.largeur)

my_rectangle = Rectangle(5,6)
print(my_rectangle.surface())
print(my_rectangle.perimeter())

print("///////////////////////////////////////////////")
class Bank:
    def __init__(self, solde ):
        self.solde = solde

    def depot(self , solde):
        return self.solde + solde

    def retret(self , solde):
        return self.solde - solde

account = Bank(5)
print(account.depot(5))
print(account.retret(5))


