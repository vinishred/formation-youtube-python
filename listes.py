

# nombre1 : int = int(input("Entrez le premier nombre: "))
# nombre2 : int = int(input("Entrez le deuxième nombre: "))

# print(f"la somme de {nombre1} et {nombre2} est {nombre1+nombre2}")

# age = int(input("Entrez votre age: "))

# majeur = True if age >= 18 else False
# print(majeur)

# for i in range(10):
#     print(f"et {i+1}")

# quand on fait un import on appelle un module
import random
import os
# ici on importe la fonction pprint dans la module pprint
from pprint import pprint

#connaitre la longueur d'une chaine de caractère
# print(len("Python"))

# connaitre la longueur d'une liste
# print(len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#création d'une liste de nombre de 0 à 9
# print(range(10))

# for i in range(7):
#     r = random.randint(0, 50)
#     print(f"et le numéro {i+1} du loto est : {r}")

# randint pour les entier
# randuniform pour les flottants
# print(random.uniform(0, 10))
#randrange pour mettre un pas 
# print(random.randrange(0, 11, 2))


# créer un dossier
# chemin = "/Users/calla/OneDrive/Bureau/SIO/Python"
# dossier = os.path.join(chemin, "testjoin")
# if not os.path.exists(dossier):
#     os.makedirs(dossier)
# else:
#     print("Le dossier existe déjà")

# supprimer un dossier
# if os.path.exists(dossier):
#     os.removedirs(dossier)
# else:
#     print("Le dossier n'existe pas")

# pour connaitre la liste des fonctions associées à un module
# pprint(dir(random))

# pour en connaitr plus sur une fonction 
# help(random.randint)

# pour savoir si une fonction est appelable si c'est true oui sinon non
# print(callable(random.randint))

# creation d'une liste
ma_premiere_liste: list = [1, 2, 3, 4.57, 5, True, 7, 8, "bonjour", 10]

# on peut accéder à un élément
# print(ma_premiere_liste[8])

#si on veut partir de la fin on fait un -1
# print(ma_premiere_liste[-1])

#on peut consulter une tranche d'éléments
# print(ma_premiere_liste[2:5])

#on peut rajouter un pas
# print(ma_premiere_liste[2:5:2])

#on peut inverser une liste
# print(ma_premiere_liste[::-1])

#on peut modifier un élément
ma_premiere_liste[0] = 0

# on peut rajouter un seul élément
ma_premiere_liste.append("dernier élément")
# print(ma_premiere_liste)

#on peut rajouter plusieurs élément à la suite
ma_premiere_liste.extend(["plusieurs", "elements"])
# print(ma_premiere_liste)

#on peut supprimer un élément par sa valeur
ma_premiere_liste.remove(4.57)  
# print(ma_premiere_liste)

#pour consulter un index dans une liste
# print(ma_premiere_liste.index(5))

#on peut supprimer un élément par son index
ma_premiere_liste.pop(4)
# print(ma_premiere_liste)

#on peut trier une liste qui a les membres du même type
ma_deuxieme_liste : list = ["b", "d", "a", "c", "e"]
# ma_deuxieme_liste.sort()

#on peut mettre le tri dans une variable
ma_deuxieme_liste_triee = sorted(ma_deuxieme_liste)
# print(ma_deuxieme_liste_triee)

ma_troisieme_liste : list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#on peut inverser une liste
ma_troisieme_liste.reverse()
# print(ma_troisieme_liste_inversee)

#methode join ppour joindre les éléments d'une liste avec un caractère spécifique
ma_liste_a_joindre: list = ["python", "est", "un", "langage", "de", "programmation"]
# print(" ".join(ma_liste_a_joindre)) 
# print("\n".join(ma_liste_a_joindre)) 

#a l'inverse on peut créer une liste à partir d'un string avec split
courses = "Riz, poisson, carottes, fenouil"
# print(courses.split(", "))

#pour savoir un élément est dans une liste
utilisateurs = ["Vincent", "Marie", "Pierre"]
# if "Vincent" in utilisateurs:
#     print("Vincent est dans la liste")
# else:
#     print("Vincent n'est pas dans la liste")

#récupérer un élément dans une liste imbriquée
liste_imbriquee = ["Vincent", ["Marie", "Pierre"]]
# print(liste_imbriquee[1][0])



