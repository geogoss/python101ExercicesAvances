from pathlib import Path

'''script pour créer un readme.txt avec python écrit dedans -> pour l'exo chercherMotDansDossier'''


dossier = Path.cwd()

p = dossier / "readme.txt"

#p.touch()

with open(p, "w") as f:
    f.write("Je kiffe le module Path de python")

with open(p, "r") as f:
    contenu = f.read()
    print(contenu)
