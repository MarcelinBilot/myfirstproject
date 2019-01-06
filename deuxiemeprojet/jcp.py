import statistics
from random import shuffle
online_player = ["Thominus","Goroky","zizi","jean"]

print(online_player)

# un jouerur se deco
del online_player[2]

print(online_player)

# suprimer toute la liste
online_player.clear()

print(online_player)

# nouvelle exemple jouer a la maitresse

notes = [8,15,20,5,18,16,]

print(notes)
shuffle(notes)
print(notes)

# module statistique
result = statistics.mean(notes)
print("la moyenne de l'élève est de {}".format(result))
