'''
083 - Recréer la méthode isdigit
Notions abordées : les fonctions, les boucles, les structures conditionnelles.

Dans cet exercice, nous allons recréer une méthode appartenant aux chaînes de caractères, la méthode isdigit,
qui permet de vérifier si une chaîne de caractères ne contient que des nombres.

Nous allons transformer cette méthode en fonction.

À vous donc de combler la fonction isdigit afin de vérifier si la chaîne de caractères que l'on passe (ici "1854274")
contient uniquement des nombres.
Votre script doit dans ce cas-ci retourner True.

Bien entendu, vous ne devez pas utiliser la méthode isdigit native de Python !

Aller plus loin : vérifiez également si l'argument passé à la fonction est bien une chaîne de caractères afin d'éviter
les erreurs (si par exemple l'utilisateur envoie une liste ou un boolean).
'''

def isdigit(nombre):
    for i in nombre:
        if i not in [str(i) for i in range(10)]:
            return False
    return True

print(isdigit("1854274"))

print(isdigit("k98643535035"))
