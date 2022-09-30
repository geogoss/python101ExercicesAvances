'''
089 - Récupérer un élément dans une liste sans causer d'erreur
Notions abordées : les listes, les fonctions, les structures conditionnelles.

Dans cet exercice, nous allons créer une fonction pour récupérer un élément dans une liste, sans causer d'erreur si
l'indice est en dehors de la liste, comme c'est le cas par défaut avec Python.

Il faut donc insérer du code dans la fonction recuperer_item pour que l'on puisse récupérer grâce à cette fonction
les éléments avec l'indice 0, 5 et -13.

Dans le premier cas, la fonction nous retournera l'élément "Julien", et dans les deux autres cas, les phrases :

Index 5 hors de la liste
Index -13 hors de la liste
La fonction aura comme premier paramètre la liste dont on veut récupérer un élément et comme deuxième paramètre
l'indice désiré.
'''
import math

def recuperer_item(liste, indice):
    if abs(indice) > len(liste) - 1:
        return "Votre indice est en dehors de la liste, adaptez le !"
    else:
        return liste[indice]


liste = ["Julien", "Marie", "Pierre"]

print(recuperer_item(liste, 0))
print(recuperer_item(liste, 5))
print(recuperer_item(liste, -13))


