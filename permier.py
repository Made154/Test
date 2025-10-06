n = int(input("Enter a number: "))
premier = True
for diviseur in range(2, n):
    reste  = n % diviseur
    if reste == 0:
        print(n, "is not a prime number", diviseur)
        premier = False

if premier:
    print(n, "is a prime number")