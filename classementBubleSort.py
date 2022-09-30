'''088 - Faire un script de tri à bulles - Code'''

def bubble_sort(liste):
    for i in range(len(liste) - 1, 0, -1):
        for j in range(i):
            n_courant = liste[j]
            n_suivant = liste[j+1]
            if n_courant > n_suivant:
                liste[j] = n_suivant
                liste[j+1] = n_courant

    return liste

l = [40, 16, 80, 2, 90]
print(bubble_sort(l))




