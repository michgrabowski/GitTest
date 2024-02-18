print ("Proste działania")

a = int(input(" Podaj pierwsza liczbe: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input ("""Wybierz rodzaj działania: 1 - dodawanie, 2 - odejmowanie
                3 - mnożenie, 4 dzielenie, 5 - potęgowanie,
                6 - pierwiastkowanie"""))

if (c == 1):
    wynik = a+b
elif (c == 2):
    wynik = a-b
elif (c == 3):
    wynik = a*b
elif (c == 4):
    wynik = a/b
elif (c == 5):
    wynik = a**b
elif (c == 6):
    wynik = abs(a/b)

print ("Wynik działania wyświetlany to:", wynik)
