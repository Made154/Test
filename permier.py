from utils import estPrmier
n = int(input("Entrez un nombre entier : "))
if estPrmier(n):
    print(n, "est un nombre premier")
else:
    print(n, "n'est pas un nombre premier")