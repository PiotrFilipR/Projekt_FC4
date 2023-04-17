import json


class Manager:

    def __init__(self):
        self.actions = {}

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb
        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Wybrano złe polecenie.")
        else:
            self.actions[name](self)


manager = Manager()

# 1. Saldo
@manager.assign("saldo")
def saldo(manager):
    with open("saldo.txt", "r") as saldo_wczytane:
        saldo = saldo_wczytane.read().strip()
        if not saldo:
            saldo = 0
        else:
            saldo = float(saldo)

    zmiana_salda_in = input("Podaj wartość kwoty dodawanej/odejmowanej z konta [PLN]: ")
    if [a for a in zmiana_salda_in if a.isdigit() or a == '.']:
        zmiana_salda = float(zmiana_salda_in)
        if zmiana_salda > 0 or zmiana_salda < 0:
            saldo += zmiana_salda
            with open("historia_operacji.txt", "a") as historia_wczytana:
                historia_wczytana.write(f"Zmiana salda: {zmiana_salda}\n")
            while saldo < 0:
                saldo -= zmiana_salda
                print("Błąd! Brak wystarczających środków na koncie!")
                pass
        else:
            print("Błąd! Podano wartość 0!")
    else:
        print("Błąd! Podano złą wartość.")
        pass

    with open("saldo.txt", "w") as saldo_wczytane:
        saldo_wczytane.write(str(saldo))

    print(f"Aktualny stan konta: {saldo} [PLN]")


# 2. Sprzedaż
@manager.assign("sprzedaz")
def sprzedaz(manager):

    with open("magazyn.txt", "r") as f:
        stan_magazynu = json.load(f)
    with open("saldo.txt", "r") as saldo_wczytane:
        saldo = saldo_wczytane.read().strip()
        if not saldo:
            saldo = 0
        else:
            saldo = float(saldo)

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
        with open("historia_operacji.txt", "a") as historia_wczytana:
            historia_wczytana.write(f"Sprzedaż: {wybrana_nazwa_sprzedaz}, {ilosc_sprzedaz}\n")
        for element in stan_magazynu:
            stan_magazynu[element] -= ilosc_sprzedaz

    print(f"Poprawnie przeprowadzono sprzedaż. \n"
          f"Aktualny stan konta: {saldo} [PLN]")

    with open("saldo.txt", "w") as saldo_wczytane:
        saldo_wczytane.write(str(saldo))

    with open("magazyn.txt", "w") as f:
        json.dump(stan_magazynu, f)


# 3. Zakup
@manager.assign("zakup")
def zakup(manager):

    with open("magazyn.txt", "r") as f:
        stan_magazynu = json.load(f)
    with open("saldo.txt", "r") as saldo_wczytane:
        saldo = saldo_wczytane.read().strip()
        if not saldo:
            saldo = 0
        else:
            saldo = float(saldo)

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
        with open("historia_operacji.txt", "a") as historia_wczytana:
            historia_wczytana.write(f"Kupno: {wybrana_nazwa_kupno}, {ilosc_kupno} \n")
        if not stan_magazynu.get(wybrana_nazwa_kupno):
            stan_magazynu[wybrana_nazwa_kupno] = ilosc_kupno
        print(f"Poprawnie przeprowadzono zakup. \n"
              f"Aktualny stan konta: {saldo} [PLN]")

    with open("saldo.txt", "w") as saldo_wczytane:
        saldo_wczytane.write(str(saldo))

    with open("magazyn.txt", "w") as f:
        json.dump(stan_magazynu, f)


# 4. Konto
@manager.assign("konto")
def konto(manager):
    with open("saldo.txt", "r") as saldo_wczytane:
        saldo = saldo_wczytane.read().strip()
        if not saldo:
            saldo = 0
        else:
            saldo = float(saldo)
    print(f"Aktualny stan konta: {saldo} [PLN]")


# 5. Lista
@manager.assign("lista")
def lista(manager):
    with open("magazyn.txt", "r") as f:
        stan_magazynu = json.load(f)

    print(f"Aktualny stan magazynu: ")
    print("*"*10)
    for i, k in stan_magazynu.items():
        print(i, k, "szt.")
    print("*" * 10)


# 6. Magazyn
@manager.assign("magazyn")
def magazyn(manager):
    with open("magazyn.txt", "r") as f:
        stan_magazynu = json.load(f)

    wybrana_nazwa_magazyn = input("Podaj nazwę produktu: ")

    if not stan_magazynu.get(wybrana_nazwa_magazyn):
        print("Brak takiego produktu!")
    else:
        print(f"Ilość {wybrana_nazwa_magazyn} na magazynie: {stan_magazynu.get(wybrana_nazwa_magazyn)} szt.")


# 7. Przegląd
@manager.assign("przeglad")
def przeglad(manager):
    with open("historia_operacji.txt.") as historia_wczytana:
        historia = historia_wczytana.readlines()

    print("Podaj zakres operacji do przeglądu, lub wstaw 0, aby wyświetlić wszystkie:")
    przeglad_1 = int(input("Podaj pierwszą operację z zakresu: "))
    przeglad_2 = int(input("Podaj drugą operację z zakresu: "))

    if przeglad_2 > 0 and przeglad_1 > 0:
        print(f"Lista operacji z zakresu {przeglad_1}-{przeglad_2} \n"
              f"{historia[przeglad_1 - 1: przeglad_2]}")
    else:
        print("*" * 10)
        print("Całkowita lista operacji: ")

        for k, v in enumerate(historia):
            print(k, v.strip())

        print("*" * 10)


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
        manager.execute('saldo')

    # 2. Sprzedaż
    elif wybor == "2":
        manager.execute('sprzedaz')

    # 3. Zakup
    elif wybor == "3":
        manager.execute('zakup')

    # 4. Konto
    elif wybor == "4":
        manager.execute('konto')

    # 5. Lista
    elif wybor == "5":
        manager.execute('lista')

    # 6. Magazyn
    elif wybor == "6":
        manager.execute('magazyn')

    # 7. Przegląd
    elif wybor == "7":
        manager.execute('przeglad')

    # 8. Koniec
    elif wybor == "8":
        break

    else:
        print("Wybrano złe polecenie.")