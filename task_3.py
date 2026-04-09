import math

bread_price = float(input ("Podaj cene chleba: "))
eggs_status = input("Czy są jajka? (tak/nie): ").lower()

if eggs_status == "tak":
    egss_price = float(input("Podaj cene za 10 jajek: "))
    print("Kup 10 jajek i chleb")
    shoping_price = bread_price+egss_price
    print(f"Cena za zakupy {shoping_price}")

elif eggs_status == "nie":
    print(f"Ok, nie kupuj jajek. \nCena zakupów {bread_price}")


