n = int(input("Enter un nombre: "))
premier = True
for diviseur in range(2, n):
    reste  = n % diviseur
    if reste == 0:
        print(n, "ce n'est pas un monbre premier", diviseur)
        premier = False

if premier:
    print(n, "c'est un nombre premier")