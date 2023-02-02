saldo = 0

stan_magazynu = {'Kolano': 12,
                 'Mufa': 21,
                 'Trójnik': 45,
                 'Kształtka': 19,
                 }

historia = []

while True:
    wybor = input("1. Saldo \n"
                  "2. Sprzedaż \n"
                  "3. Zakup \n"
                  "4. Konto \n"
                  "5. Lista \n"
                  "6. Magazyn \n"
                  "7. Przegląd \n"
                  "8. Koniec \n"
                  "Wciśnij odpowiednią liczbę, aby wybrać polecenie... "
                  )

    # 1. Saldo

    if wybor == "1":
        zmiana_salda = float(input("Podaj wartość kwoty dodawanej/odejmowanej z konta [PLN]: "))
        if zmiana_salda > 0 or zmiana_salda < 0:
            saldo += zmiana_salda
            historia.append(f"Zmiana salda: {zmiana_salda}")
            while saldo < 0:
                saldo -= zmiana_salda
                print("Błąd! Brak wystarczających środków na koncie!")
                break
        else:
            print("Błąd! Podano wartość 0!")

        print(f"Aktualny stan konta: {saldo} [PLN]")

    # 2. Sprzedaż

    elif wybor == "2":

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
            historia.append(f"Sprzedaż: {wybrana_nazwa_sprzedaz}, {ilosc_sprzedaz}")
            for element in stan_magazynu:
                stan_magazynu[element] -= ilosc_sprzedaz

        print(f"Poprawnie przeprowadzono sprzedaż. /n"
              f"Aktualny stan konta: {saldo} [PLN]")

    # 3. Zakup

    elif wybor == "3":

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
            historia.append(f"Kupno: {wybrana_nazwa_kupno}, {ilosc_kupno}")
            if not stan_magazynu.get(wybrana_nazwa_kupno):
                stan_magazynu[wybrana_nazwa_kupno] = ilosc_kupno

        print(f"Poprawnie przeprowadzono zakup. /n"
              f"Aktualny stan konta: {saldo} [PLN]")

    # 4. Konto

    elif wybor == "4":
        print(f"Aktualny stan konta: {saldo} [PLN]")

    # 5. Lista

    elif wybor == "5":
        print(f"Aktualnny stan magazynu: {stan_magazynu}")

    # 6. Magazyn

    elif wybor == "6":

        wybrana_nazwa_magazyn = input("Podaj nazwę produktu: ")

        if not stan_magazynu.get(wybrana_nazwa_magazyn):
            print("Brak takiego produktu!")
        else:
            print(f"Ilość {wybrana_nazwa_magazyn} na magazynie: {stan_magazynu.get(wybrana_nazwa_magazyn)} szt.")

    # 7. Przegląd

    elif wybor == "7":

        print("Podaj zakres operacji do przeglądu, lub wstaw 0, aby wyświetlić wszystkie:")
        przeglad_1 = int(input("Podaj pierwszą operację z zakresu: "))
        przeglad_2 = int(input("Podaj drugą operację z zakresu: "))

        if przeglad_2 > 0 and przeglad_1 > 0:
            print(f"Lista operacji z zakresu {przeglad_1}-{przeglad_2} \n"
                  f"{historia[przeglad_1 - 1 : przeglad_2]}")
        else:
            print(historia)

    # 8. Koniec

    elif wybor == "8":
        break

    else:
        print("Wybrano złe polecenie.")
