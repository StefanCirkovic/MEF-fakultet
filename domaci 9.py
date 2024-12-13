
# Domaci 9


import math






# 1.zadatak:


def pravougaonik(m, n):

    for i in range(m):
        print("*" * n)


pravougaonik(4, 10)






# 2.zadatak:

def promeni_velicinu(string):

    return string.swapcase()


rezultat = promeni_velicinu("MAJICA")
print(rezultat)






# 3.zadatak:


def n(string_1, string_2):
    if len(string_1) == len(string_2):
        return True
    else:
        return False


result = n("majica", "majica")
print(result)






# 4.zadatak:

def hipotenuza(a, b):

    c = math.sqrt(a**2 + b**2)
    return int(c)


result = hipotenuza(3, 4)
print(result)

    












        
    
    
