# Domaci 5


# 1. zadatak:

i = 1

while i <= 50:
    print(i)
    i += 1


# 2. zadatak:

string = "tekst"

i = 0

while i < len(string):
    print(string[i])
    i += 1

# 2. zadatak b):

i = 0

while i < len(string):
    print(string[i])
    i += 2

# 3. zadatak:

kg = -1

while kg < 0:
    kg = int(input("Unesite neku tezinu u kg: "))
    if kg < 0:
        print("Greska")
    else:
        pound = kg * 2.2
        print(f" Tezina {kg} kg u funtama je {pound} ")


# 4. zadatak:


correct_password = "password"

attempts = 0

max_attempts = 5

while attempts < max_attempts:
    password = input("Unesite lozinku: ")
    if password == correct_password:
        print("Ulogovali ste se")
        break
    else:
        attempts += 1
        if attempts < max_attempts: # ovaj uslov sam dodao da mi ne bi nakon petog pokusaja izbacalo "Uneli ste pogresnu lozinku, molim Vas unesite ponovo" i ovo:"Premasili ste dozvoljen broj pokusaja, pokusajte ponovo kasnije" vec samo da sam premasio broj pokusaja i da pokusam ponovo kasnije, kako se ne bi desio dupli odgovor koji nam se desavao na predavanju.  
            print("Uneli ste pogresnu lozinku, molim Vas unesite ponovo")

if attempts == max_attempts:
    print("Premasili ste dozvoljen broj pokusaja, pokusajte ponovo kasnije")
    




        













        
