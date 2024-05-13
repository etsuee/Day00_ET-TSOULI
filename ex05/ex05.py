import random

random_tab = [random.randint(1,100) for i in range(18)]

def ordre_decroissant(tab):
    for i in range(1, len(tab)):
        valeur_courante = tab[i]
        position = i

        while position > 0 and tab[position - 1] < valeur_courante:
            tab[position] = tab[position - 1]
            position -= 1

        tab[position] = valeur_courante

ordre_decroissant(random_tab)
print(random_tab)