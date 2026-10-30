import machine
import time

def silnia_iter(n):
    if type(n) is not int or n < 0:
        raise ValueError("Niepoprawny argument")
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik

def silnia_rek(n):
    if type(n) is not int or n < 0:
        raise ValueError("Niepoprawny argument")
    if n <= 1:
        return 1
    return n * silnia_rek(n - 1)

def testy():
    assert silnia_iter(0) == 1
    assert silnia_rek(0) == 1
    assert silnia_iter(1) == 1
    assert silnia_rek(1) == 1
    assert silnia_iter(5) == 120
    assert silnia_rek(5) == 120
    assert silnia_iter(6) == silnia_rek(6)
    
    blad = False
    try:
        silnia_iter(-1)
    except ValueError:
        blad = True
    assert blad

    blad = False
    try:
        silnia_rek(-67)
    except ValueError:
        blad = True
    assert blad

    for funkcja in (silnia_iter, silnia_rek):
        blad = False
        try:
            funkcja("abc")
        except ValueError:
            blad = True
        assert blad

        blad = False
        try:
            funkcja(2.5)
        except ValueError:
            blad = True
        assert blad

    print("Testy OK")

def main():
    print("Przyklady:")
    for x in (3, 5, 10):
        print("{0}! = {1}".format(x, silnia_iter(x)))

    n_pomiar = 100
    powtorzenia = 1000

    t0 = time.ticks_ms()
    for i in range(powtorzenia):
        silnia_iter(n_pomiar)
    t1 = time.ticks_ms()
    czas_iter = time.ticks_diff(t1, t0)

    t0 = time.ticks_ms()
    for i in range(powtorzenia):
        silnia_rek(n_pomiar)
    t1 = time.ticks_ms()
    czas_rek = time.ticks_diff(t1, t0)

    print("Wersja iteracyjna: {0} ms".format(czas_iter))
    print("Wersja rekurencyjna: {0} ms".format(czas_rek))

    while True:
        try:
            wejscie = input("Podaj liczbe calkowita (q to quit): ").strip()
            if wejscie.lower() == "q":
                break
            n = int(wejscie)
            if n < 0:
                print("Blad: liczba musi byc nieujemna")
                continue
            print("{0}! (iteracyjnie) = {1}".format(n, silnia_iter(n)))
            try:
                print("{0}! (rekurencyjnie) = {1}".format(n, silnia_rek(n)))
            except RecursionError:
                print("Blad: przekroczono limit zaglebienia rekurencji dla silnia_rek({0})".format(n))
        except ValueError:
            print("Blad: wprowadzona wartosc nie jest liczba calkowita")

if __name__ == "__main__":
    testy()
    main()
