def estPrmier(n):
    for diviseur in range(2, n):
        reste  = n % diviseur
        if reste == 0:
            return False

    return True