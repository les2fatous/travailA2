import random


def words():
    mots = []
    with open("mots.txt") as file:
        for ligne in file:
            mots.append(ligne.rstrip("\n"))

    return mots


def affiche():
    print("Bienvenue dans le jeu LET-GET\n")
    print("Vous avez 6 tentatives \nVous avez 3 points d'erreur")
    print("\n\n\t\t+---+\n\t\t|   |\n\t\t    |\n\t\t    |\n\t\t    |\n\t\t    |\n\t===========\n\n")


def choisir(mots):
    niveau = int(input("Choisir un niveau de 1 à 3: "))
    while 3 < niveau or niveau < 1:
        niveau = int(input("Choisir un niveau de 1 à 3: "))

    print(f"Vous avez choisi le niveau {niveau}")
    mot = random.choice(mots)


    if niveau == 1:
        while 4 < len(mot):
           mot = random.choice(mots)

        print(f"Je vous propose un mot de {len(mot)} lettres")
        return mot

    else:
        if niveau == 2:
            while len(mot)>7 or len(mot)<5:
                mot = random.choice(mots)

            print(f"Je vous propose un mot de {len(mot)} lettres")
            return mot
        else:
            while len(mot) < 7:
                mot = random.choice(mots)

            print(f"Je vous propose un mot de {len(mot)} lettres")
            return mot


def test(mot):

    lettres = []
    av = 3
    erreur = 0

    corp = [" ", " ", " ", " ", " ", " "]
    pendu = ["o", "/", "|", "\\", "/", "\\"]

    for l in mot:
        lettres.append("_")

    print(" ".join(lettres))
    while erreur < 6:

        lettre = input("\nEntrez une lettre: ")

        """ vérifier si l'utilisateur a entré une lettre alphabétique si non un avertissement lui sera donné et un point d'erreur de moins"""

        while len(lettre) > 1 or ord(lettre) < 65 or ord(lettre) > 122:
            print("Vous devez saisir une lettre")
            av -= 1
            print(f"Il vous reste {av} avertissements")
            if av == 0:
                erreur += 1
                print(f"Il vous reste {6-erreur} tentatives")
                av = 3
            lettre = input("\nEntrez une lettre: ")

        if lettre in mot:
            """ Tester si la lettre existe déjà dans le tableau lettres si oui un avertissement sera donné et un point d'erreur de moins"""
            if lettre not in lettres:
                print("Bravo, lettre correcte\n")
                nbre = 0

                """ Recupérer les lettres trouvées dans le tableau lettres """
                for l in mot:
                    if lettre == l:
                        lettres[nbre] = lettre
                    nbre+=1

                """ si la lettre est correcte un poin d'erreur lui est ajouté s'il avait perdu un point d'erreur"""
                if av < 3:
                    av += 1
            else:
                print("Lettre déjà trouvée\n")
                av -= 1
                print(f"Il vous reste {av} avertissements")

        else:
            """Affichage du pendu"""
            n = testLettre(lettre)
            """Incrémenter le nombre d'erreur de n selon la nature de la lettre alphabétique entrée"""
            erreur += n


            """Calcul du nombre tentatives restant"""
            reste = 6-erreur

            if reste > 0:
                print(f"Il vous reste {reste} tentatives")

            else:
                print("Il vous reste 0 tentative")

            if n == 2:
                if reste == -1:
                    erreur -= 1

                corp[erreur-2] = pendu[erreur-2]

            corp[erreur-1] = pendu[erreur-1]
            print("\n\n +---+")
            print(" |   |")
            print(" {}   |".format(corp[0]))
            print("{}{}{}  |".format(corp[1], corp[2], corp[3]))
            print("{} {}  |".format(corp[4], corp[5]))
            print("=========\n")

        print(" ".join(lettres))
        if '_' not in lettres:
            print("Félicitation vous avez deviné le mot\n")
            points = score(reste, occurence(mot))
            print(f"Votre score est : {points}")
            if len(lettres)<5:
                niveau = 1
            else:
                if len(lettres)<=7:
                    niveau = 2
                else:
                    niveau = 3

            enregistrer(niveau, reste, points)
            break

    """Test si le mot est trouvé ou pas"""
    if '_' in lettres:
        print("\nVous avez perdu")
        print(f"\nLe mot à déviner était : {mot}")






"""Tester si la lettre entrée par l'utilisateur est une consonne  ou une voyelle et retourner le nombre d'erreur correspondant"""

def testLettre(l):
    lettres = ['a', 'e', 'o', 'i', 'u', 'y']
    if l in lettres:
        print("\nVous avez saisi une voyelle qui n'est pas dans le mot\n\nVous perdez 2 tentatives")
        return 2
    else:
        print("Vous avez saisi une consonne qui n'est pas dans le mot\nVous perdez 1 tentative")
        return 1

def occurence(mot):
    unique = []
    for i in range(0, len(mot)):
        if mot[i] not in unique:
            unique.append(mot[i])
    return len(unique)

def score(reste, unique):
    return reste * unique




def enregistrer(niveau, reste, points):
    with open("log_game.txt", "a") as fichier:
        fichier.write(f"Niveau : {niveau}\nNombre de tentatives restantes : {reste}\nScore : {points}")
