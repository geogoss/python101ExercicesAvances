'''
090 - Recréer la méthode replace - Code
'''

def replace(phrase, mot_a_remplacer, nouveau_mot):
    while mot_a_remplacer in phrase:
        debut = phrase.index(mot_a_remplacer)
        fin = debut + len(mot_a_remplacer)

        phrase = list(phrase)
        phrase[debut:fin] = list(nouveau_mot)
        phrase = "".join(phrase)

    return phrase

phrase = replace("Mon nom est Bond, James Bond.", "Bond", "Tuche")
print(phrase)





