
saldo = 0

stan_magazynu = {'Kolano': 12,
                 'Mufa': 21,
                 'Trójnik': 45,
                 'Kształtka': 19,
                 }

# 1. Saldo

zmiana_salda = float(input("Podaj wartość kwoty dodawanej/odejmowanej z konta [PLN]: "))

if zmiana_salda > 0 or zmiana_salda < 0:
    saldo += zmiana_salda
    while saldo < 0:
        saldo -= zmiana_salda
        print("Błąd! Brak wystarczających środków na koncie!")
        break
else:
    print("Błąd! Podano wartość 0!")

print(f"Aktualny stan konta: {saldo} [PLN]")

# 2. Sprzedaż

wybrana_nazwa_sprzedaz = input("Podaj nazwę sprzedawanego produktu: ")
if not stan_magazynu.get(wybrana_nazwa_sprzedaz):
    print("Brak takiego produktu")

cena_sprzedaz = float(input("Podaj cenę jednostkową [PLN]: "))
if cena_sprzedaz <= 0:
    print("Podano błędną cenę")

ilosc_sprzedaz = int(input("Podaj ilość sztuk: "))
if ilosc_sprzedaz <= 0:
    print("Podano błędną ilość")
elif stan_magazynu.get(wybrana_nazwa_sprzedaz) <= 0:
    print("Brak towaru na magazynie")
elif ilosc_sprzedaz > stan_magazynu.get(wybrana_nazwa_sprzedaz):
    print("Brak wystarczającej ilości towaru na magazynie")

else:
    saldo += (cena_sprzedaz * ilosc_sprzedaz)
    for element in stan_magazynu:
        stan_magazynu[element] -= ilosc_sprzedaz

print(f"Poprawnie przeprowadzono sprzedaż. /n"
      f"Aktualny stan konta: {saldo} [PLN]")


# 3. Zakup

wybrana_nazwa_kupno = input("Podaj nazwę kupowanego produktu: ")


cena_kupno = float(input("Podaj cenę jednostkową [PLN]: "))
if cena_kupno <= 0:
    print("Podano błędną cenę.")

ilosc_kupno = int(input("Podaj ilość sztuk: "))
if ilosc_kupno <= 0:
    print("Podano błędną ilość.")
elif cena_kupno * ilosc_kupno >= saldo:
    print("Brak wystarczających środków na zakup.")
else:
    saldo -= (cena_kupno * ilosc_kupno)
    if not stan_magazynu.get(wybrana_nazwa_kupno):
        stan_magazynu[wybrana_nazwa_kupno] = ilosc_kupno

print(f"Poprawnie przeprowadzono zakup. /n"
      f"Aktualny stan konta: {saldo} [PLN]")

# 4. Konto

print(f"Aktualny stan konta: {saldo} [PLN]")

# 5. Lista

print(f"Aktualnny stan magazynu: {stan_magazynu}")

# 6. Nowy artykuł magazyn

nowy_produkt = input("Podaj nazwę produktu: ")

stan_magazynu[nowy_produkt] = int(input("Podaj ilość nowych produktów: "))
print(f'Pomyślnie dodano do magazynu "{nowy_produkt}"')

# 7. Magazyn

wybrana_nazwa_magazyn = input("Podaj nazwę produktu: ")

if not stan_magazynu.get(wybrana_nazwa_magazyn):
    print("Brak takiego produktu!")
else:
    print(f"Ilość {wybrana_nazwa_magazyn} na magazynie: {stan_magazynu.get(wybrana_nazwa_magazyn)} szt.")

# 8. Przegląd

# 9. Koniec
