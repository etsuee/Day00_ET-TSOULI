
def num_armstrong():
    num = int(input("Entrez un numéro: "))
    
    somme = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        somme += digit ** 3
        temp //= 10

    if num == somme:
        print(num,"est un numéro d'Armstrong")
    else:
        print(num,"n'est pas un numéro Armstrong")

num_armstrong()