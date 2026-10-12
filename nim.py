#PROGRAMME PRINCIPAL

from asyncio import wait_for
from time import *
from constantes import *
from fonctions_affichage import *
from fonctions_jeu import *

while True:
    print("                    "
          "                    ")

    """Afficher le joueur qui joue"""
    joueur_1 = choisir_depart()
    if joueur_1 == HOMME :
        print("Le joueur choisis est l'homme")

    elif joueur_1 == MACHINE:
        print("Le joueur choisi est l'ordinateur")

    nb_restantes = ALLUMETTES
    while est_gagnant(nb_restantes) == False:
        print(afficher_allumettes(nb_restantes))
        nb_retirees = choisir_nb_retrait(joueur_1, nb_restantes)
        print(afficher_choix(joueur_1, nb_retirees))
        nb_restantes = retirer_allumettes(nb_restantes, nb_retirees)
        joueur_1 = changer_joueur(joueur_1)
        sleep(0.5)
    print(afficher_gagnant(joueur_1))
    if choix_joueur_recommencer() != True:
        print("Fin de la partie")
        break  #Quittez la boucle




