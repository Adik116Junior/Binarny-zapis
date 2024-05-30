def liczba_na_binarne(liczba):
    if isinstance(liczba, int):
        return bin(liczba)[2:]
    else:
        raise ValueError("Podana wartość nie jest liczbą całkowitą")
liczba = int(input("Podaj liczbę całkowitą: "))
wynik_binarny = liczba_na_binarne(liczba)
print(f"Liczba {liczba} w zapisie binarnym to: {wynik_binarny}")
