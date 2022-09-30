'''
084 - Recréer la méthode join
Notions abordées : les fonctions.

On continue avec les fonctions et méthodes de base que l'on essaie de comprendre et de recréer. Cette fois-ci, on s'intéresse à
la méthode join qui permet de joindre plusieurs éléments d'une liste par une chaîne de caractères.

Nous allons donc recréer cette méthode et la transformer en fonction. Votre fonction devra prendre comme premier
argument l'élément avec lequel vous voulez séparer les éléments de votre liste.

À la place d'une liste, nous passerons ici directement à la fonction des chaînes de caractères à joindre.

Votre fonction devra donc être appelée de la façon suivante :

join(":", "Bonjour", "tout", "le", "monde")

Et retournera la chaîne de caractère suivante :

"Bonjour:tout:le:monde"

Votre fonction devra fonctionner avec autant de chaînes de caractères que voulu par l'utilisateur et bien entendu,
interdit d'utiliser la méthode join !
'''

def join(*args):
    contenu = ""
    separateur = args[0]
    elements = args[1:]

    for element in elements:
        contenu += element + separateur

    return contenu[:-1]


j = join(":", "Bonjour", "tout", "le", "monde")
print(j)

test = join(" ", "Petit", "test", ",", "pour", "voir", "si", "ça", "fonctionne", "bien")
print(test)


