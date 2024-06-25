def ask_password()->None:
    mdp_trop_court = "votre mot de passe est trop court."
    mdp_sans_chiffre = "votre mot de passe ne contient pas de chiffre."
    mdp_sans_lettres = "votre mot de passe ne contient pas de lettre."
    password = str(input("Entrez un mot de passe (min 8 caracères): "))
    if len(password) == 0:
        print(mdp_trop_court.upper())
        ask_password()
    elif len(password) < 8:
        print(mdp_trop_court.capitalize())
        ask_password()
    elif password.isdigit():
        print(mdp_sans_lettres.capitalize())
        ask_password()
    elif password.isalpha():
        print(mdp_sans_chiffre.capitalize())
        ask_password()
    else:    
        print("Inscription terminée.")


ask_password()
