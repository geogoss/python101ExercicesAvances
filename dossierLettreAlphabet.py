'''
085 - Créer un dossier pour chaque lettre de l'alphabet - Code
'''

import os
import string

dossier = os.path.dirname(__file__)
dossier_a_creer = os.path.join(dossier, "alphabet")

for lettre in string.ascii_uppercase:
    lettre_dir = os.path.join(dossier_a_creer, lettre)
    if not os.path.isdir(lettre_dir):
        os.makedirs(lettre_dir)

