a = int(input("Podaj 1 liczbe: "))
b = int(input("Podaj 2 liczbe: "))

c = input("Co chcesz robic?")

if c == "obliczenia":
    d = input("Co dokladnie?")
    if d == "dodawanie":
        e = int(a+b)
        print(e)
    if d == "odejmowanie":
        e = int(a-b)
        print(e)
    if d == "mnożenie":
        e = int(a*b)
        print(e)
    if d == "dzielenie":
        e = int(a/b)
        print(e)
