# random_number = int(input("Podaj jakąś liczbę całkowitą: "))
# x2random_number = 2 * random_number
# if x2random_number > 100:
#     numberminus100 = x2random_number - 50
#     print(numberminus100)
# else:
#     print(x2random_number)
#
#______________________________________________________________
# random_number = int(input("Podaj jakąś liczbę całkowitą: "))
# if random_number % 2 == 0:
#     print("Jest podzielna przez 2")

#______________________________________________________
# random_number = int(input("Podaj jakąś liczbę całkowitą: "))
# if random_number % 2 == 0:
#     print("Jest podzielna przez 2")
# else:
#     print("Nie jest podzielna przez 2")

#___________________________________________
# random_number = int(input("Podaj jakąś liczbę całkowitą: "))
# if random_number % 2 == 0 or random_number % 3 == 0:
#     print("Jest podzielna przez 2 lub 3")
# _________________________________________

# random_number = int(input("Podaj jakąś liczbę całkowitą: "))
# if random_number % 2 == 0 or random_number % 3 == 0:
#     print("Jest podzielna przez 2 lub 3")
# elif random_number % 5 == 0:
#     print("Jest podzielna przez 5")
# elif random_number % 7 == 0:
#     print("Jest podzielna przez 7")
# ___________________________________

# random_number = int(input("Podaj jakąś liczbę całkowitą: "))
# if random_number % 5 == 0 or random_number % 7 == 0:
#     print("Jest podzielna przez 5 lub 7")
# elif random_number % 5 == 0:
#     print("Jest podzielna przez 5")
# elif random_number % 7 == 0:
#     print("Jest podzielna przez 7")
# ________________________________________


random_number = int(input("Podaj jakąś liczbę całkowitą: "))
if random_number % 5 == 0:
    print("Jest podzielna przez 5")
    random_number_minus_5 = random_number - 5
    if random_number_minus_5 < 0:
        print("Liczba po odjeciu 5 jest mniejsza od 0")
    elif random_number_minus_5 == 0:
        print("Liczba po odjeciu 5 jest równa 0")
    elif random_number_minus_5 > 0:
        print("Liczba po odjeciu 5 jest większa od 0")
