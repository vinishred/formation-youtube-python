# import random
# import sys

# TITRE = """
# ***  le jeu du nombre mystère ***
# Arriveras tu à deviner le nombre en moins de 5 tentatives ?
# """
# NOMBRE_MYSTERE = random.randint(1, 21)
# print(NOMBRE_MYSTERE)
# nombre_utilisateur = ""
# nombre_essai = 5

# print(TITRE)
# while nombre_utilisateur != NOMBRE_MYSTERE and nombre_essai > 0:
#     print(f"Il te reste {nombre_essai} essais")
#     nombre_utilisateur = int(input("choisis un nombre entre 1 et 20 : "))
#     nombre_essai -= 1
# if nombre_essai == 0:
#     print(f"Dommage... tu as perdu, le nombre mystère était {NOMBRE_MYSTERE}")
#     sys.exit()
# else:
#     print("Bravo!! Tu as gagné")


#Correction
from random import randint

number_to_find = randint(1, 20)
remaining_attempts = 5

print(" Le jeu du nombre mystère ")

while remaining_attempts > 0:
    print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")
    guess = input("choisis un nombre entre 1 et 20 : ")
    if not guess.isdigit():
        print("Veuillez rentrer un nombre valide")
        continue
    guess = int(guess)
    if guess < number_to_find:
        print(f"Le nombre mystère est plus grand que {guess}")
    elif guess > number_to_find:
        print(f"Le nombre mystère est plus petit que {guess}")
    else:
        print(f"Bravo!! Tu as gagné le nombre mystère était bien {number_to_find}")
        break
    remaining_attempts -= 1
if remaining_attempts > 0:
    print(f"Félicitations tu as trouvé en {6 - remaining_attempts} essai{'s' if (6 - remaining_attempts) > 1 else ''}")
else:
    print(f"Dommage... tu as perdu, le nombre mystère est {number_to_find}")