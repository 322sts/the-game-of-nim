#FONCTIONS JEU (Alban)

from random import *
from constantes import *

def choisir_depart():
    """
    rôle : Sélectionne le joueur qui commence la partie.

    paramètres : aucun

    renvoie un entier (0 : HOMME, 1 : MACHINE)
    """

    return randint(0, 1)


def est_gagnant(nb_restantes: int) -> bool:
    """
    rôle : Vérifie s’il reste des allumettes

    paramètres : nb_restantes (int) : nombre d’allumettes restantes

    renvoie True si le nombre d’allumettes est nul, False
    sinon.
    """

    if nb_restantes <= 0:
        return True
    elif nb_restantes != 0:
        return False




def choisir_nb_retrait(joueur: int, nb_restantes: int) -> int:
    """
    rôle : - Si pour l’homme, demande le nombre d’allumettes à retirer (dans les limites possibles).
           - Si pour la machine, choisit le nombre au hasard (dans
           les limites possibles)

    paramètres : - joueur (int) : 0 (HOMME) ou 1 (MACHINE)
                 - nb_restantes (int) : nombre d’allumettes restantes

    renvoie un entier : le nombre d’allumettes choisies
    """

    if joueur == HOMME:
        nombre_choisis_homme = int(input("Choisissez un nombre entre 1 et 3   "))
        while nombre_choisis_homme < 1 or nombre_choisis_homme > 3 or nombre_choisis_homme > nb_restantes:
            print("Votre nombre n'est pas compris entre 1 et 3 compris, ou vous avez choisis d'enlever plus d'allumettes que celles restantes ! Veuillez réessayer")
            nombre_choisis_homme = int(input("Choisissez un nombre entre 1 et 3   "))
        nb_retirees = nombre_choisis_homme
        return nb_retirees

    else:
        # La machine ne doit jamais retirer plus
        # d'allumettes qu'il n'en reste (plafond = nb_restantes).
        nb_retirees = randint(1, min(3, nb_restantes))
        return nb_retirees


def retirer_allumettes(nb_restantes: int, nb_retirees: int) -> int:
    """
        rôle : Retire les allumettes choisies du nombre total
               restant.

        paramètres : - nb_restantes (int) : nombre d’allumettes restantes
                     - nb_retirees (int) : nombre d’allumettes choisies

        renvoie un entier : le nombre d’allumettes restantes
                            après le retrait
    """
    nb_restantes = nb_restantes - nb_retirees
    return nb_restantes


def changer_joueur(joueur: int) -> int:
    """
        rôle : Change le joueur en cours (0 ou 1)

        paramètres : - joueur (int) : 0 (HOMME) ou 1 (MACHINE)

        renvoie un entier : 0 (HOMME) ou 1 (MACHINE)
    """
    if joueur == 0:
        joueur += 1
        return joueur
    elif joueur == 1:
        joueur -= 1
        return joueur

def choix_joueur_recommencer() -> bool:
    """
        rôle : Savoir si l'utilisateur veut relancer une partie

        paramètres : aucun

        renvoie un booléen : True ou False

    """
    choix_recommencer = input("Voulez vous rejouer ?? Entrez : Oui/Non")
    if choix_recommencer == str("Oui"):
        return True

    elif choix_recommencer == str("Non"):
        return False

