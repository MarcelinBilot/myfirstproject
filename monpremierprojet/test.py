# recolter une valeur porte monnaie
porte_monnaie = int(input("Combien avez vous d'argent dans votre porte monnaie"))

# creer un produit qui aura comme valeur 50
produit = int(input("Comboien coûte votre produit"))
print("Le produit coûte " + str(produit) + "€ ")

# afficher la nouvelle valeur du porte monnaie, apres l'achat
porte_monnaie = (porte_monnaie - produit)

print("Il ne te reste plus que " + str(porte_monnaie) + "€ après ton achat !")
