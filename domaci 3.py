
from random import randint



# 1. zadatak
user = int(input("Unesite duzinu u centimetrima: "))

if user < 0:
    print("Uneli ste losu vrednost")
else:
    print(user / 2.54)

# 2.zadatak



temperature = float(input("Unesite temperaturu: "))

temperature_unit = input("U kojoj je jedinici temperatura? (C za Celsius, F za Fahrenheit): ")

if temperature_unit == 'C':

    converting_from_C_to_F = ( 9 /5) * temperature + 32
    print(f"{temperature}°C je {converting_from_C_to_F}°F.")
elif temperature_unit == 'F':

    converting_from_F_to_C = ( 5 /9) * (temperature - 32)
    print(f"{temperature}°F je {converting_from_F_to_C}°C.")
else:
    print("Greska")


#  3. zadatak

temperature = float(input("Unesite temperaturu u celzijusima: "))

if temperature < -273.15:
    print("Temp je neispravna jer je ispod nule")
elif temperature == -273.15:
    print("Temperatura je na apsolutnoj 0.")
elif -273.14 <= temperature < 0:
    print("Temperatura je ispod tačke mržnjenja.")
elif temperature == 0:
    print("Temperatura je na tački mržnjenja.")
elif 0 < temperature < 100:
    print("Temperatura je u normalnom opsegu.")
elif temperature == 100:
    print("Temperatura je na tački varenja.")
else:
    print("Temperatura je iznad tačke varenja.")




#  4.zadatak


random_number = randint(1 ,10)

number = int(input("Unesite neki broj"))

if random_number == number:
    print("Pogodili ste!")
else:
    print(f"niste pogodili, broj je {random_number}")

# dodatni zadaci

# zadatak 1


godina = int(input("Unesite godinu: "))


if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
    print(f"{godina} je prestupna godina.")
else:
    print("Nije prestupna godina")



# 2.zadatak


number = int(input("Unesite broj: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(i)



# 3.zadatak


questions = 10
for question in range(1, questions + 1):
    first_number = randint(1, 10)
    second_number = randint(1, 10)
    result = first_number * second_number

    math_question = int(input(f"Zadatak {question}: {first_number} * {second_number} = "))

    if math_question == result:
        print("Vas rezultat je tacan!")
    else:
        print(f"Netacno, tacan rezultat je: {math_question}.")

# 4.zadatak


products_amount = int(input("Koliko proizvoda kupujete: "))

if products_amount < 10:
    total_price = products_amount * 12
    print(f"Vasa ukupna cena iznosi {total_price} dolara")
elif 10 <= products_amount < 99:
    total_price = products_amount * 10
    print(f"Vasa ukupna cena iznosi {total_price} dolara")
elif products_amount >= 100:
    total_price = products_amount * 7
    print(f"Vasa ukupna cena iznosi {total_price} dolara")
