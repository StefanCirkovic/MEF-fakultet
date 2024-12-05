

# 1.zadatak:

products = {}

while True:
    name = input("Unesite ime proizvoda: ")
    if name == "":
        break

    price = input(f"Unesite cenu proizvoda {name}: ")
    products[name] = price


while True:
    searched_product = input("Unesite ime proizvoda iz recnika: ")

    if searched_product == "":
        break
    elif searched_product in products:
        print(f"Cena proizvoda {searched_product} je {products[searched_product]} din. ")
    else:
        print("Ovaj proizvod ne postoji u recniku.")
        

# 2.zadatak:

value = int(input("Unesite neku cenu: "))

print("Proizvodi koji sadrze manju cenu od vaseg unosa su: ")
for name in products:
    if int(products[name]) < value:
        print(f"{name} : {products[name]} din. ")


# 3.zadatak:

users = {
    "marko": "1234",
    "ana": "pass123",
    "jovana": "sifra321",
    "petar": "lozinka567",
    "milica": "luda_osoba",
    "ivan": "asdfgh",
    "nikola": "zxcvbn",
    "sofija": "password",
    "vladimir": "12345",
    "marija": "lozinka" 
    }


name = input("Unesite ime korisnika: ")

password = input("Unesite sifru: ")

if name in users:
    if users[name] == password:
        print("Uspesno ste se ulogovali")
    else:
        print("Neispravna sifra")
else:
    print("Korisnik nije registrovan u sistemu.")




# 4.zadatak:


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union = A | B

intersection = A & B

print(f"Unija A i B je {union}")

print(f"Presek A i B je {intersection}")
            





















    

    
