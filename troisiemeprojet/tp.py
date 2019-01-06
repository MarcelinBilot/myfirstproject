# tp : une fonction pour calculer le nombre de voyelles dans un mot

# definir une fonction get_vowels_numbers(mot)
def get_voyels_number(word):
    # créer un compteur de voyelles
    nb_vowels = 0

    # pour chaque lettre du mot vous verifiez s'il s'agit d'un voyelle
    for letter in ['a', 'e', 'i', 'o', 'u', 'y']:
        # si c'est le cas
        if letter in vowels:
            # on ajoute un au compteur
            nb_vowels += 1

    # à la fin de la fonction, vous allez renvoyer le compteur
    return nb_vowels


word = input("Entrer un mot")
vowels_count = get_vowels_numbers()
print("Il y a ", vowels_count, "dans le mot", word)﻿