from fonctions_jeu import *
from fonctions_affichage import *
from constantes import *

val = choisir_depart()
assert val == HOMME or val == MACHINE, "Initialisation du joueur"
assert est_gagnant(0) == True, "Vérification du nombre d'allumettes"
assert est_gagnant(3) == False, "Vérification du nombre d'allumettes"
assert changer_joueur(HOMME) == MACHINE, "Changement de joueur"
assert changer_joueur(MACHINE) == HOMME, "Changement de joueur"

choix10 = choisir_nb_retrait(MACHINE, 10)
assert choix10 > 0 and choix10 <= 3, "Choix du nombre à retirer"
choix2 = choisir_nb_retrait(MACHINE, 2)
assert choix2 > 0 and choix2 <= 2, "Choix du nombre à retirer"

print("Entrez la valeur 2")
choix10_homme = choisir_nb_retrait(HOMME, 10)
assert choix10_homme > 0 and choix10_homme <= 3, "Choix du nombre à retirer"
print("Entrez la valeur 2")
choix2_homme = choisir_nb_retrait(HOMME, 2)
assert choix2_homme > 0 and choix2_homme <= 2, "Choix du nombre à retirer"

assert retirer_allumettes(10, 3) == 7, "Retrait des allumettes"
assert retirer_allumettes(2, 2) == 0, "Retrait des allumettes"
assert afficher_allumettes(5) == " | | | | |", "Affichage allumettes"
                                                                 