from math import sqrt

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
        print(f"Kérem {t.__name__}-t adjon meg!")
        return safeInput(text, t, sign)


print("------ 1. ------")
egyikSzam = safeInput("Kérlek add meg az első számot: ")
masikSzam = safeInput("Kérlek add meg a második számot: ")

b = egyikSzam > 0 and masikSzam > 0
print(f"Mindkét szám pozitív: {b}")

igazE = egyikSzam < 4 and masikSzam != 6
print(f"Az egyik < 4 és a másik != 6: {igazE}")

vanNulla = egyikSzam == 0 or masikSzam == 0
print(f"Bármelyik szám egyenlő nullával: {vanNulla}")

felt1 = egyikSzam == 5 or masikSzam != 4
print(f"Az első 5-ös vagy a másik nem 4-es: {felt1}")

felt2 = egyikSzam <= 5 or masikSzam >= 13
print(f"Az első nemnagyobb 5-nél vagy a másik nemkisebb 13-nál: {felt2}")

felt3 = (egyikSzam > 0 and masikSzam < 0) or (egyikSzam < 0 and masikSzam > 0)
print(f"Az egyik szám pozitív, a másik negatív: {felt3}")


print("------ 2. ------")
print("A\tB\tA AND B\tA OR B\tA XOR B")
print("-" * 35)
for A in [False, True]:
    for B in [False, True]:
        and_res = A and B
        or_res = A or B
        xor_res = A != B
        print(f"{A}\t{B}\t{and_res}\t{or_res}\t{xor_res}")


print("------ 3. ------")
num = safeInput("Kérlek adj meg egy egész számot: ")
rem = num % 10
print(f"A szám 10-zel vett osztási maradéka: {rem}")
if num % 10 == 0:
    print("A szám osztható 10-zel.")


print("------ 4. ------")
szamlalo = safeInput("Kérlek add meg a számlálót: ")
nevezo = safeInput("Kérlek add meg a nevezőt: ")
if nevezo == 0:
    print("Hiba: A tört nevezője nem lehet nulla!")
else:
    print(f"A tört értéke: {szamlalo / nevezo}")


print("------ 5. ------")
num = safeInput("Kérlek adj meg egy háromjegyű pozitív egész számot: ", int, 1)
if 100 <= num <= 999:
    s = str(num)
    szamjegyek_kobe = int(s[0])**3 + int(s[1])**3 + int(s[2])**3
    if szamjegyek_kobe == num:
        print(f"A {num} egy Armstrong-szám.")
    else:
        print(f"A {num} nem Armstrong-szám.")
else:
    print("A megadott szám nem háromjegyű!")


print("------ 6. ------")
num = safeInput("Kérlek adj meg egy egész számot: ")
if num == 4:
    print("A megadott szám a 4-es.")
if num < 10:
    print("A megadott szám kisebb mint 10.")
if num % 2 == 0:
    print("A megadott szám páros.")
if 0 <= num <= 10:
    print("A megadott szám a [0,10] intervallumba esik.")
if num % 3 == 0 and num % 5 == 0:
    print("A megadott szám osztható 3-mal és 5-tel is.")
if not (10 <= num <= 20):
    print("A megadott szám nem a [10,20] intervallumba esik.")


print("------ 7. ------")
num1 = safeInput("Kérlek add meg az első számot: ")
num2 = safeInput("Kérlek add meg a második számot: ")

if num1 == num2:
    print("A két szám egyenlő.")
if num1 % 2 != 0 and num2 % 2 != 0:
    print("Mind a két szám páratlan.")
if num1 % 3 == 0 or num2 % 3 == 0:
    print("Legalább az egyik szám osztható hárommal.")
if num1 < 0 and num2 < 0:
    print("Mind a két szám negatív.")
if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
    print("Az egyik szám negatív, a másik szám pozitív.")


print("------ 8. ------")
a = safeInput("Adj meg a téglalap 'a' oldalát: ", float, 1)
b = safeInput("Adj meg a téglalap 'b' oldalát: ", float, 1)
if a == b:
    print("A megadott alakzat egy négyzet.")
else:
    print("A megadott alakzat egy téglalap.")


print("------ 9. ------")
a = safeInput("Adj meg az első oldalt: ", float, 1)
b = safeInput("Adj meg a második oldalt: ", float, 1)
c = safeInput("Adj meg a harmadik oldalt: ", float, 1)
if a == b == c:
    print("Ez egy szabályos háromszög.")
else:
    print("Ez nem szabályos háromszög.")


print("------ 10. ------")
num = safeInput("Kérlek adj meg egy egész számot: ")
if num == 10 or num == 100 or num == 1000:
    print(f"A szám egyenlő {num}-zel/zal.")
else:
    print("A szám nem egyenlő sem 10-zel, sem 100-zal, sem 1000-rel.")


print("------ 11. ------")
num = safeInput("Kérlek adj meg egy számot: ", float)
if 1 <= num <= 9:
    print("A szám benne van az [1,9] intervallumban.")
else:
    print("A szám nincs benne az [1,9] intervallumban.")


print("------ 12. ------")
num = safeInput("Kérlek adj meg egy egész számot: ")
if num < 0 and num % 2 != 0:
    print("A szám negatív páratlan szám.")
else:
    print("A szám nem negatív páratlan szám.")


print("------ 13. ------")
a = safeInput("Adj meg az első számot (osztó): ")
b = safeInput("Adj meg a második számot: ")
if a != 0 and b % a == 0:
    print(f"A(z) {a} osztója a(z) {b} számnak.")
else:
    print(f"A(z) {a} nem osztója a(z) {b} számnak.")


print("------ 14. ------")
num = safeInput("Kérlek adj meg egy számot: ", float)
if num >= 0:
    print(f"A szám gyöke: {sqrt(num)}")
else:
    print("Hiba: Negatív számból nem vonható négyzetgyök!")


print("------ 15. ------")
a = safeInput("Adj meg az 'a' oldalt: ", float, 1)
b = safeInput("Adj meg a 'b' oldalt: ", float, 1)
c = safeInput("Adj meg a 'c' oldalt: ", float, 1)

if (a + b > c) and (a + c > b) and (b + c > a):
    print(f"A megadott adatokból képezhető háromszög. Kerülete: {a + b + c}")
else:
    print("Hibás adatok! A megadott szakaszokból nem építhető háromszög.")


print("------ 16. ------")
s = safeInput("Adja meg a megtett távolságot (km): ", float, 1)
t = safeInput("Adja meg az eltelt időt (óra): ", float, 1)
if t > 0:
    v = s / t
    if v > 145 or v < 80:
        print("Nem megfelelő sebességgel közlekedett!")
    else:
        print("Minden rendben!")
else:
    print("Az időnek nagyobbnak kell lennie 0-nál!")


print("------ 17. ------")
num = safeInput("Kérlek adj meg egy egész számot: ")
if num > 0:
    print("A szám előjele: pozitív (+)")
elif num < 0:
    print("A szám előjele: negatív (-)")
else:
    print("A szám értéke nullával egyenlő.")


print("------ 18. ------")
a = safeInput("Adja meg az első számot: ", float)
b = safeInput("Adja meg a második számot: ", float)
if a > b:
    print(f"{a} nagyobb mint {b}")
elif a < b:
    print(f"{a} kisebb mint {b}")
else:
    print(f"{a} egyenlő {b}-vel")


print("------ 19. ------")
temp = safeInput("Adja meg a víz hőmérsékletét (°C): ", float)
if temp <= 0:
    print("Halmazállapot: szilárd (jég)")
elif temp < 100:
    print("Halmazállapot: folyékony (víz)")
else:
    print("Halmazállapot: légnemű (gőz)")


print("------ 20. ------")
x = safeInput("Adja meg az X koordinátát: ", float)
y = safeInput("Adja meg az Y koordinátát: ", float)

if x > 0 and y > 0:
    print("Első síknegyed (+, +)")
elif x < 0 and y > 0:
    print("Második síknegyed (-, +)")
elif x < 0 and y < 0:
    print("Harmadik síknegyed (-, -)")
elif x > 0 and y < 0:
    print("Negyedik síknegyed (+, -)")
else:
    print("A pont valamelyik koordináta-tengelyen vagy az origóban fekszik.")