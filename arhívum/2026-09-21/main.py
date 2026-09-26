from math import pi

def safeInput(text, t=int, sign=0):
    try:
        temp = t(input(text))
        if sign == 1 and temp < 0:
            print("kérem adjon meg pozitív számot")
            return safeInput(text, t, sign)
        elif sign == -1 and temp > 0:
            print("kérem adjon meg negatív számot")
            return safeInput(text, t, sign)
        return temp
    except ValueError:
        print(f"Kérem {t}-t adjon meg!")
        return safeInput(text, t, sign)


print("------ 1. ------")
a = safeInput("Kérlek add meg az első számot: ")
b = safeInput("Kérlek add meg a második számot: ")
print(f"A két szám öszege: {a + b}")
print(f"A két szám különbsége: {a - b}")
del(a)
del(b)

print("------ 2. ------")
f = safeInput("Kérlek adj meg egy valós számot: ", float)
print(f"A szám tízszerese: {f * 10}")

print("------ 3. ------")
s = safeInput("Kérlek add meg a megtett távolságot (km): ", float)
t = safeInput("Kérlek add meg az időt (óra): ", float)
print(f"az átlagsebesség: {s/t}")

print("------ 4. ------")
b = safeInput("Kérlek add meg a háromszög alapját: ")
m = safeInput("Kérlek add meg a magasságot: ")
print(f"A háromszög területet: {(b*m)/2}")

print("------ 5. ------")
intager = safeInput("Kérlek adj meg egy egész számot: ")
print(f"A szám kétszerese: {intager * 2}")

print("------ 6. ------")
num = safeInput("Kérlek adj meg egy valós számot: ")
print(f"A szám négyzetet: {intager ** 2}")
print(f"A szám köbe: {intager ** 3}")

print("------ 7. ------")
Celsius = safeInput("Kérlek adj meg a hőmérsékletet: ")
print(f"Fahrenheit = {Celsius * 9/5 + 32}")

print("------ 8. ------")
a = safeInput("Kérlek add meg az alapot: ")
b = safeInput("Kérlek add meg a kitevőt: ")
print(f"az eredmény: {a ** b}")

print("------ 9. ------")
a = safeInput("Kérlek add meg az első számot: ")
b = safeInput("Kérlek add meg a második számot: ")
print(f"az eredmény: {a * 2 + b / 2}")

print("------ 10. ------")
s = safeInput("Kérlek add meg a megtett távolságot (km): ", float, 1)
fogy = safeInput("adja meg a fogyasztást(l/km): ", float, 1)
print(f"{s * fogy}l benzint fogyasztott")

print("------ 11. ------")
ber = safeInput("adja meg az órabért: ", float, 1)
t = safeInput("adja meg a munkaidőt: ", float, 1)
print(f"a bér {ber *t}Ft")

print("------ 12. ------")
r = safeInput("adja meg a kör sugarát: ", float, 1)
print(f"A kör kerülete: {2 * pi * r}")

print("------ 13. ------")
age = safeInput("Adja meg az életkorát: ", int, 1)
avgSleep = safeInput("adja meg hány órát alszij átlagosan: ", float, 1)
print(f"havonta kb. {30.5 * avgSleep}")

print("------ 14. ------")
step = safeInput("adja meg a lépésszámot: ", int, 1)
avg_step = safeInput("adja meg az átlagos lépésszámát: ", int, 1)
print(f"kb. {avg_step * 7} lépést tesz meg hetente")

print("------ 15. ------")
class Targy:
    def __init__(self, nev:str, ar:int):
        self.ar = ar
        self.nev = nev

class Diak:
    def __int__(self, nev:str, zsebpenz:int):
        self.nev = nev
        self.zsebpenz

    def calcTargy(self, targy:Targy):
        temp = 0
        i = 0
        while temp >= targy.ar:
            temp += self.ar
            i += 1
        return i

p = Diak(input("adja meg a nevét: "), safeInput("adja meg a zsebpénzét: ", int, 1))
t = Targy(input("adja meg a tárgyat amire gyüjt: "), safeInput("Adja meg az árát: ", int, 1))
print(f"Kendes {p.nev}! Az átlad gyüjtött tárgyat({t.nev}) {p.calcTargy(t)} zseppénzciklus után tudnád megvenni.")

print("------ 16. ------")
m = safeInput("Adja meg a sulyát: ", int, 1)
l = safeInput("Adja meg a magaságát", int, 1)

print(f"BMI: {m / (l**2)}")

print("------ 17. ------")
cel_m = safeInput("Adja meg a cél sulyát: ", int, 1) 
rate = (m - cel_m)/3
for i in range(3)
    print(f"{i}. hét {m - (1 + i) * rate}")

print("------ 18. ------")
lencse = safeInput("Adja meg a lencsék árát", sign=1)
keret = safeInput("Adja meg a keret árát", sign=1)
age = safeInput("Adja meg az életkorát: ", int, 1)
kedv = keret / 100 * age
print(f"""
Ön a szemüvegkeret árából, ami {keret}, {age} kedvezményt kap!
A szemüveglencse ára: {lencse}
----------------------------
Szemüvege vételára: {keret - kedv + lencse}
""")
