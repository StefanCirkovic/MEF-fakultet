# Domaci 7:

import random


# 1.zadatak:


numbers_list = input("Unesite listu celih brojeva, odvojene razmacima: ").split()



numbers_list = [int(i) for i in numbers_list]


# a)

print(len(numbers_list))



# b)

print(numbers_list[-1])





# c)

print(list(reversed(numbers_list)))




# d)

if 5 in numbers_list:
    print("DA")
else:
    print("NE")




# e)

print(numbers_list.count(5))





# f)

del numbers_list[0]
del numbers_list[-1]
numbers_list.sort()
print(numbers_list)





# g)

count = 0

for number in numbers_list:
    if number < 5:
        count += 1
print(f"brojevi manji od 5 u listi: {count}")




# 2.zadatak:

random_numbers_list = []

for i in range(20):
    random_numbers_list.append(random.randint(1,100))






# a)

print(random_numbers_list)
        





# b)

print(f"Ukupna suma: {sum(random_numbers_list)}")


print(f"prosecna vrednost je: {sum(random_numbers_list)/20}")






# c:


print(random_numbers_list)
print(min(random_numbers_list))
print(max(random_numbers_list))





# d:


even_numbers = []

for number in random_numbers_list:
    if number % 2 == 0:
        even_numbers.append(number)

print(f"Parni brojevi: {even_numbers}")





# 3. zadatak:


new_list = [8, 9, 10]



# a)

new_list[1] = 17
print(new_list)




# b)


new_list.append(4)
new_list.append(5)
new_list.append(6)
print(new_list)


# c)


del new_list[0]
print(new_list)



# d)

new_list.sort()
print(new_list)




# e)

new_list = new_list * 2
print(new_list)




# f)


new_list.insert(3, 25)
print(new_list)


print(new_list)





# 4. zadatak:


another_new_list = input("Unesite listu koja sadrzi brojeve od 1 do 12, sa razmacima: ").split()

another_new_list = [int(number) for number in another_new_list]
                       

for number in range(len(another_new_list)):
    if another_new_list[number] > 10:
        another_new_list[number] = 10

print(another_new_list)
        
        











