Magda_points =[6, 7, 0, 6, 0, 6, 4, 0, 7]
Przemek_points = [0, 5, 6, 2, 0, 4, 0, 6, 9]

Magda_suma = 0
Przemek_suma = 0
for round in range (len(Magda_points)):
    Magda_suma +=Magda_points[round]
    Przemek_suma += Przemek_points[round]
    print(f"Runda {round +1} \nMagda ilość punktów {Magda_points[round]}"
          f"\nPrzemek ilość punktów {Przemek_points[round]}")
    print(f"Suma Magdy: {Magda_suma}\nPrzemek_suma: {Przemek_suma}")
if Magda_suma > Przemek_suma:
    print("Gre wygrała Magda")
elif Przemek_suma > Magda_suma:
    print("Gre wygrał Przemek")
else:
    print("Był remis")