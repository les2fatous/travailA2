import random
import maLibrairie

continuer = 'o'
while continuer == 'o':
    mots = maLibrairie.words()
    maLibrairie.affiche()
    mot = maLibrairie.choisir(mots).lower()
    maLibrairie.test(mot)

    continuer = input("\nSi vous voulez continuer tapez o : ")

print("\nVous avez quitté le jeu")