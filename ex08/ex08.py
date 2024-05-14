def pyramide(n):
    for i in range(1, n+1):
        nb_etoiles = 2*i - 1
        espace_gauche = ' ' * (n - i)
        ligne = espace_gauche + '*' * nb_etoiles
        print(ligne)

while True:
    try:
        nombre_lignes = int(input("Entrez le nombre de lignes pour la pyramide d'étoiles : "))
        break
    except ValueError:
        print("Veuillez entrer un entier.")

pyramide(nombre_lignes)