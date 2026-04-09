def task_1():
    random_number = int(input("Podaj jakąś liczbę całkowitą: "))
    x2random_number = 2 * random_number
    if x2random_number > 100:
        numberminus100 = x2random_number - 50
        print(numberminus100)
    else:
        print(x2random_number)
# task_1()

def task_2():
    random_number = int(input("Podaj jakąś liczbę całkowitą: "))
    if random_number % 2 == 0:
        print("Jest podzielna przez 2")
# task_2()

def task_3():
    random_number = int(input("Podaj jakąś liczbę całkowitą: "))
    if random_number % 2 == 0:
        print("Jest podzielna przez 2")
    else:
        print("Nie jest podzielna przez 2")
# task_3()

def task_4():
    random_number = int(input("Podaj jakąś liczbę całkowitą: "))
    if random_number % 2 == 0 or random_number % 3 == 0:
        print("Jest podzielna przez 2 lub 3")
#task_4()

def task_5():
    random_number = int(input("Podaj jakąś liczbę całkowitą: "))
    if random_number % 2 == 0 or random_number % 3 == 0:
        print("Jest podzielna przez 2 lub 3")
    elif random_number % 5 == 0:
        print("Jest podzielna przez 5")
    elif random_number % 7 == 0:
        print("Jest podzielna przez 7")
#task_5()
def task_6():
    random_number = int(input("Podaj jakąś liczbę całkowitą: "))
    if random_number % 5 == 0 or random_number % 7 == 0:
        print("Jest podzielna przez 5 lub 7")
    elif random_number % 5 == 0:
        print("Jest podzielna przez 5")
    elif random_number % 7 == 0:
        print("Jest podzielna przez 7")
#task_6()

def task_7():
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
task_7()