import random
import sys
def battle_random() -> None:
    ENNEMY_HEALTH : int = 50
    PLAYER_HEALTH : int = 50
    NUMBER_OF_POTIONS : int = 3
    SKIP_TURN : bool = False
    ENNEMY_LIST : list = ["Gobelin", "Nain", "Sorcier", "Voleur", "Assassin", "Magicien", "Chevalier", "Barbare"] 

    INTRODUCTION = """
    Bienvenue dans battle random, un jeu de combat dans lequel vous devez combattre un ennemi.
    Vous pourrez attaquer un ennemi ou prendre une potion de soin.
    Attention, si vous prenez une potion de soin vous passerez votre tour sur le prochain tour.
    Réduisez l'énergie de votre ennemi à 0 pour gagner le combat.
    Bonne chance !!"""

    SCRIPT = """
    Souhaitez-vous attaquer l'ennemi ou prendre une potion de soin ?
    1. Attaquer 🗡️
    2. Prendre une potion de soin 🍶"""


    print("-"*30)
    print("⚔️  Bienvenue dans battle random  ⚔️!")
    print("-"*30)
    player_name : str = input("Quel est ton nom jeune guerrier? ").capitalize()
    if player_name == "":
        player_name = "Joueur"

    print("-"*30)
    print(f"Bonjour {player_name} !!")
    #choix aléatoire dans la liste d'ennemis
    ennemi_choice = random.choice(ENNEMY_LIST)
    print(INTRODUCTION)
    print(f"Tu vas devoir affronter l'ennemi suivant: {ennemi_choice}")

    while True:
        if PLAYER_HEALTH > 0 and ENNEMY_HEALTH > 0:
            if SKIP_TURN:
                print("Vous passez votre tour.")
                ennemy_attack = random.randint(0, 10)
                print(f"{ennemi_choice} t'attaque avec une attaque de {ennemy_attack} points de force. 💘")
                PLAYER_HEALTH -= ennemy_attack
                SKIP_TURN = False
            else:
                print("-"*30)
                print("Tes points de vie actuels: ", PLAYER_HEALTH)
                print("Tes potions restantes : ", NUMBER_OF_POTIONS)
                print(f"Points de vie de {ennemi_choice} :  {ENNEMY_HEALTH}")
                print(SCRIPT)
                choice = int(input())

                if choice == 1:
                    print("Tu as choisi d'attaquer")
                    player_attack = random.randint(0, 10)
                    print(f"{player_name} attaque {ennemi_choice} avec une attaque de {player_attack} points de force.⚔️")
                    ENNEMY_HEALTH -= player_attack

                    ennemy_attack = random.randint(0, 10)
                    print(f"{ennemi_choice} t'attaque avec une attaque de {ennemy_attack} points de force. 💘")
                    PLAYER_HEALTH -= ennemy_attack

                elif choice == 2:   
                    if NUMBER_OF_POTIONS > 0:
                        print("Tu as choisi de prendre une potion de soin")
                        NUMBER_OF_POTIONS -= 1
                        healing = random.randint(5, 20)
                        print(f"{player_name} prend une potion de soin et regagne {healing} points de vie.")
                        PLAYER_HEALTH += healing
                        ennemy_attack = random.randint(0, 10)
                        print(f"{ennemi_choice} t'attaque avec une attaque de {ennemy_attack} points de force.💘")
                        PLAYER_HEALTH -= ennemy_attack
                        SKIP_TURN = True
                    else:
                        print("Tu n'as plus de potion de soin.🌚")
                else:
                    print("Choix invalide")
                    print("-"*30)
        elif PLAYER_HEALTH <= 0:
            print(f"Dommage {player_name} ! Tu as été vaincu par {ennemi_choice}.😞")
            break
        elif ENNEMY_HEALTH <= 0:
            print(f"Bien joué {player_name} ! Tu as vaincu {ennemi_choice}.🥳")
            break
    print("Fin du jeu")
    try_again = input("Voulez-vous rejouer ? (O/N) ").upper()
    if try_again == "O":
        battle_random()
    else:
        sys.exit()

    
battle_random()
