def calculatrice():
    operation : str = input("Choisissez l'opération que vous voulez effectuer (addition: 1, soustraction: 2, multiplication: 3, division:4): ")

    if operation == "1":
        addition()
    elif operation == "2":
        soustraction()
    elif operation == "3":
        multiplication()
    elif operation == "4":
        division()
    else:
        print("Veuillez entrer une opération valide.")
        calculatrice()

def addition():
    nombre_1 : str = ""
    nombre_2 : str = ""
    print("Entrez deux nombres pour calculer leur somme.")
    while not nombre_1.isdigit() :
        nombre_1 = input("Entrez le premier nombre: ")
        if not nombre_1.isdigit():
            print("Veuillez rentrer un nombre valide.")
    while not nombre_2.isdigit() :
        nombre_2 = input("Entrez le deuxième nombre: ")
        if not nombre_2.isdigit():
            print("Veuillez rentrer un nombre valide.")
    try:
        print("La somme de", nombre_1, "et", nombre_2, "est", int(nombre_1) + int(nombre_2))
    except:
        print("Il semble s'être produit une erreur.")
    else:   
        continuer : str = str(input("Voulez-vous continuer (O/N) ? ")).upper()
        if continuer == "O":
            calculatrice()
        else:
            print("Ok , Au revoir !")

def soustraction():
    nombre_1 : str = ""
    nombre_2 : str = ""
    print("Entrez deux nombres pour calculer leur soustraction.")
    while not nombre_1.isdigit() :
        nombre_1 = input("Entrez le premier nombre: ")
        if not nombre_1.isdigit():
            print("Veuillez rentrer un nombre valide.")
    while not nombre_2.isdigit() :
        nombre_2 = input("Entrez le deuxième nombre: ")
        if not nombre_2.isdigit():
            print("Veuillez rentrer un nombre valide.")
    try:
        print("La soustraction de", nombre_1, "et", nombre_2, "est", int(nombre_1) - int(nombre_2))
    except:
        print("Il semble séré produire une erreur.")
    else:   
        continuer : str = str(input("Voulez-vous continuer (O/N) ? ")).upper()
        if continuer == "O":
            calculatrice()
        else:
            print("Ok , Au revoir !")

def multiplication():
    nombre_1 : str = ""
    nombre_2 : str = ""
    print("Entrez deux nombres pour calculer leur multiplication.")
    while not nombre_1.isdigit() :
        nombre_1 = input("Entrez le premier nombre: ")
        if not nombre_1.isdigit():
            print("Veuillez rentrer un nombre valide.")
    while not nombre_2.isdigit() :
        nombre_2 = input("Entrez le deuxième nombre: ")
        if not nombre_2.isdigit():
            print("Veuillez rentrer un nombre valide.")
    try:
        print("La multiplication de", nombre_1, "et", nombre_2, "est", int(nombre_1) * int(nombre_2))
    except:
        print("Il semble séré produire une erreur.")
    else:   
        continuer : str = str(input("Voulez-vous continuer (O/N) ? ")).upper()
        if continuer == "O":
            calculatrice()  
        else:
            print("Ok , Au revoir !")

def division():
    nombre_1 : str = ""
    nombre_2 : str = ""
    print("Entrez deux nombres pour calculer leur division.")
    while not nombre_1.isdigit() :
        nombre_1 = input("Entrez le premier nombre: ")
        if not nombre_1.isdigit():
            print("Veuillez rentrer un nombre valide.")
    while not nombre_2.isdigit() :
        nombre_2 = input("Entrez le deuxième nombre: ")
        if not nombre_2.isdigit():
            print("Veuillez rentrer un nombre valide.")
    try:
        print("La division de", nombre_1, "et", nombre_2, "est", int(nombre_1) / int(nombre_2))
    except:
        print("Il semble séré produire une erreur.")
    else:   
        continuer : str = str(input("Voulez-vous continuer (O/N) ? ")).upper()
        if continuer == "O":
            calculatrice()  
        else:
            print("Ok , Au revoir !")
            

calculatrice()