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

    blad = False
    try:
        silnia_iter("abc")
    except ValueError:
        blad = True
    assert blad

    print("Testy OK")

def main():
    print("Przyklady:")
    for x in (3, 5, 10):
        print(f"{x}! = {silnia_iter(x)}")

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

    print(f"Wersja iteracyjna: {czas_iter} ms")
    print(f"Wersja rekurencyjna: {czas_rek} ms")

    while True:
        try:
            liczba = int(input("Podaj liczbe calkowita wieksza od 0: "))
            n = liczba
            if n < 0:
                print("Blad: liczba musi byc nieujemna")
                continue
            print(f"{n}! (iteracyjnie) = {silnia_iter(n)}")
            print(f"{n}! (rekurencyjnie) = {silnia_rek(n)}")
        except ValueError:
            print("Blad: wprowadzona wartosc nie jest liczba calkowita")
        except (EOFError, KeyboardInterrupt):
            break

testy()
main()
