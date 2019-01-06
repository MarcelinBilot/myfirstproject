
# creer une fonctioin max() qui va renvoyer le resultat le plus haut parmis 2 valeurs
def max(a, b):
    if a > b:
        return a
    else:
        return b


first_value = int(input("Entrer la valeur de a (la premiere)"))
second_value = int(input("Enter la valeur b (la seconde)"))
max_value = max(first_value, second_value)
print("La valeur max est", max_value)