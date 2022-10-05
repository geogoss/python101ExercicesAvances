'''
091 - Créer une classe personnalisée pour une chaîne de caractère
Notions abordées : les classes, les méthodes.

Dans cet exercice, on continue avec les classes et les méthodes.

L'objectif est de créer une classe qui va nous permettre d'utiliser des noms de méthodes francisés à la place des
méthodes de base de Python qui sont en anglais.

Les trois méthodes que nous allons recréer sont : upper, lower et capitalize qui ont comme effet respectivement,
de mettre le texte en majuscule, en minuscule, et en format 'titre' (première lettre en majuscule, le reste en minuscule).

Le but de l'exercice n'est pas de recréer l'algorithme des fonctions anglaises mais juste d'appeler les fonctions upper,
lower et capitalize dans des méthodes francisés. Si vous souhaitez cependant complexifier l'exercice, vous pouvez vous
amuser à recréer l'algorithme de ces fonctions en plus.

Nous allons appeler ces fonctions respectivement majuscule, minuscule et titre.

Votre script devra donc printer la chaîne de caractère en majuscule, en minuscule et en titre de cette façon :

#>>> print(chaine.majuscule())
"UDEMY"
#>>> print(chaine.minuscule())
"udemy"
#>>> print(chaine.titre())
"Udemy"
'''


class SuperChaine(object):
    def __init__(self, texte):
        self.texte = texte

    def majuscule(self):
        return self.texte.upper()

    def minuscule(self):
        return self.texte.lower()

    def titre(self):
        return self.texte.capitalize()


chaine = SuperChaine("udemy")
print(chaine.majuscule())
print(chaine.minuscule())
print(chaine.titre())