# liste_de_courses : list = []
# def market_drive()->None:
#     user_choice : str = input("\n\nChoisissez parmis les 5 options suivantes : \n 1. Ajouter un article à la liste \n 2. Retirer un article de la liste \n 3. Afficher la liste \n 4. Vider la liste \n 5. Quitter \n\n\n Votre choix ici :")
#     if user_choice == "1": 
#         add_article = input("Ajouter un article à la liste: ")
#         liste_de_courses.append(add_article)
#         print(f"L'article {add_article} a été ajouté à la liste.")
#         market_drive()
#     elif user_choice == "2":
#         delete_article = input("Retirer un article de la liste: ")
#         if delete_article in liste_de_courses:
#             liste_de_courses.remove(delete_article)
#         else:
#             print("Cet article n'est pas dans la liste")
#         market_drive()
#     elif user_choice == "3":
#         print("Liste des articles dans la liste :")
#         if len(liste_de_courses) == 0:
#             print("Votre liste ne contient aucun élément.")
#         else:
#             for index, value in enumerate(liste_de_courses):
#                 print(f"{index+1}. {value}")
#         market_drive()
#     elif user_choice == "4":
#         #on veut vider notre liste
#         #on peut utiliser la fonction clear
#         liste_de_courses.clear()
#         print("La liste a été vidée de son contenu.")
#         market_drive()
#     elif user_choice == "5":
#         print("A bientôt !")
#     else:
#         print("Choix invalide")
#         market_drive()


# market_drive()

#correction
import sys

LISTE = []

MENU = """Choisissez parmis les 5 options suivantes :
1. Ajouter un article à la liste
2. Retirer un article de la liste
3. Afficher la liste
4. Vider la liste
5. Quitter
👉 Votre choix ici : 
"""

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = ""

    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Choix invalide. Veuillez reéssayer.")

    if user_choice == "1":
        add_article = input("Ajouter un article à la liste: ")
        LISTE.append(add_article)
        print(f"L'article {add_article} a été ajouté à la liste.")
    elif user_choice == "2":
        delete_article = input("Retirer un article de la liste: ")
        if delete_article in LISTE:
            LISTE.remove(delete_article)
        else:
            print("Cet article n'est pas dans la liste")
    elif user_choice == "3":
        print("Liste des articles dans la liste :")
        if len(LISTE) == 0:
            print("Votre liste ne contient aucun élément.")
        else:
            for index, value in enumerate(LISTE, start=1):
                print(f"{index}. {value}")
    elif user_choice == "4":
        LISTE.clear()
        print("La liste a été vidée de son contenu.")
    elif user_choice == "5":
        print("A bientôt !")
        sys.exit()

    print("-" * 40)

