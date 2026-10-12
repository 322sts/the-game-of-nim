#FONCTIONS AFFICHAGE

from constantes import *


def afficher_allumettes(nb_restantes :int) -> str :
    """
    Crée une ligne de nb barres verticales.

    Parametres :
        nb_restantes (int) : nombres d'allumettes restantes

    Renvoie une chaine de caractères composée de barres verticales
    """
    barres = " |"
    nb_barres = barres * nb_restantes
    return nb_barres



def afficher_choix(joueur: int, choisir_nb_retrait: int) -> str :
    """
    Construit une phrase qui annonce le nombre d'allumette choisies par le joueur en cours

    Parametres:
    joueur (int): 0 (HOMME) ou 1 (MACHINE)
    choix (int) : nb d'allumettes choisies
    """
    if joueur == HOMME :
        joueur_allumette ="Homme"
    elif joueur == MACHINE:
        joueur_allumette ="Machine"

    return joueur_allumette + " a choisi : "+ str(choisir_nb_retrait)




def afficher_gagnant(joueur: int) -> str:
    """
    Construit une phrase qui annonce le gagnant.

    Parametres:
    joueur (int) : 0(HOMME) ou 1 (MACHINE)

    Renvoie :
    str : la phrase construite
    """
    if joueur == HOMME :
        gagnant = "Homme"
    elif joueur == MACHINE:
        gagnant = "Machine"
    return "Le gagnant est : " + str(gagnant)