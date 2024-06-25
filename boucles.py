#la boucle for
#parcourir une boucle
movie_list : list = ["star wars", "titanic", "the avengers", "the exorcist", "Harry Potter"]
# for movie in movie_list:
#     print(movie)

# pour répéter une action un très grand nombre de fois on utilise range(x)
# for i in range(10):
#     print(f"Utilisateur {i+1}")
#autre solution
# for i in range(1, 11):
#     print(f"Utilisateur {i}")

liste_nombres : list = [-2, -5, -3, 0, 1, 2, 3, 4, 5]
nombres_positifs : list = []
#2 façons de l'écrire avec une boucle for
#soit avec la compréhension de liste
# nombres_positifs : list = [i for i in liste_nombres if i > 0]
#soit par une boucle for
# for nombre in liste_nombres:
#     if nombre > 0:
#         nombres_positifs.append(nombre)

#soit avec la compréhension de liste avec else
# nombres_positifs : list = [i if i > 0 else -i for i in liste_nombres]
# soit par une boucle for avec else
# for nombre in liste_nombres:
#     if nombre > 0:
#         nombres_positifs.append(nombre)
#     else :
#         nombres_positifs.append(-nombre)
# print(nombres_positifs)

#on veut afficher le mot python à l'envers
mot : str = "python"
# reversed_list =list(reversed(mot))
for lettre in reversed(mot):
    print(lettre)




#la boucle while
# i : int = 0
# while i < 10:
#     print(f"i est égale à {i} qui est inférieur à 10 donc ce texte s'affiche.")
#     i = i + 1

import time
# while True:
#     print("sauvegarde en cours")
#     time.sleep(10)

# user_continue = "O"
# while user_continue == "O":
#     print("Ok on continue !")
#     user_continue = str(input("Voulez-vous continuer (O/N) ? ")).upper()
