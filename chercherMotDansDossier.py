'''
086 - Chercher un mot dans des fichiers - Code
'''
from glob import glob
import os
from pathlib import Path

dossier = Path(Path.cwd().parent.parent)
mot = "python"

fichiers = glob(f"{dossier}/**/*.txt", recursive=True)
fichiers_trouves = []

for i in fichiers:
    with open(i,"r") as f:
        contenu = f.read()
        if mot in contenu:
            fichiers_trouves.append(i)

print(fichiers_trouves)



