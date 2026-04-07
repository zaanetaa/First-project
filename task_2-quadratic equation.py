import math
def delta_calculation():
    a = int(input("Podaj pierwszą wartość "))
    b = int(input("Podaj drugą wartość "))
    c = int(input("Podaj trzecią wartość "))
    print(f"Twoje wartości to {a}, {b}, {c}")
    delta = b*b - 4*a*c
    print(f"Delta = {delta}")
    if delta == 0:
       x = ((-b/2) * a)
       print(f"Delta ma jedno rozwiązanie x = {x}")
    elif delta > 0:
       x1 = (-b - math.sqrt(delta)) / (2 * a)
       x2 = (-b + math.sqrt(delta)) / (2 * a)
       print(f"Delta ma dwa rozwiązania x1 = {x1} i x2 = {x2}")
    else:
        print("Brak rozwiązań w zbiorze liczb rzeczywistych")



delta_calculation()
