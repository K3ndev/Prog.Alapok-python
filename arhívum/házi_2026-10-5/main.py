import random
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
n1 = safeInput("Kérlek adj meg egy számot 1 és 10 között: ", int, 1)
if 1 <= n1 <= 10:
    for i in range(1, n1 + 1):
        print(f"{i}. Sok beszédnek sok az alja.")
else:
    print("A számnak 1 és 10 között kell lennie!")


print("------ 2. ------")
n2 = safeInput("Kérlek adj meg egy számot 1 és 10 között: ", int, 1)
if 1 <= n2 <= 10:
    for i in range(1, n2 + 1):
        print(f"Megmondtam már {i}-szer, hogy semmit sem mondok el kétszer!")
else:
    print("A számnak 1 és 10 között kell lennie!")


print("------ 3. ------")
print("0-tól 50-ig:")
for i in range(51):
    print(i, end=" ")
print()

print("182-től 212-ig:")
for i in range(182, 213):
    print(i, end=" ")
print()

print("Páros számok 100-tól 200-ig:")
for i in range(100, 201, 2):
    print(i, end=" ")
print()

print("Páratlan számok 89-től 57-ig visszafelé:")
for i in range(89, 56, -2):
    print(i, end=" ")
print()

print("1-től 20-ig a számok és négyzetük:")
for i in range(1, 21):
    print(f"{i} -> {i**2}")

print("99-től csökkenő sorrendben 3-mal osztható pozitívak:")
for i in range(99, 0, -3):
    print(i, end=" ")
print()

print("101-től 50-ig csökkenőben az öttel oszthatóak kétszerese:")
for i in range(100, 49, -1):
    if i % 5 == 0:
        print(i * 2, end=" ")
print()

print("1-től 1000-ig vesszővel, végén ponttal:")
out_str = ""
for i in range(1, 1001):
    if i == 1000:
        out_str += f"{i}."
    else:
        out_str += f"{i}, "
print(out_str)

print("1000-től 1-ig 3-asával visszafelé:")
for i in range(1000, 0, -3):
    print(i, end=" ")
print()


print("------ 4. ------")
print("100 db csillag:")
print("*" * 100)

db = safeInput("Add meg a darabszámot: ", int, 1)
char = input("Add meg a karaktert: ")
print(char * db)

szoveg = input("Adj meg egy szöveget keretezéshez: ")
keret = "*" * (len(szoveg) + 4)
print(keret)
print(f"* {szoveg} *")
print(keret)

print("8x8-as sakktábla:")
for sor in range(8):
    sor_str = ""
    for oszlop in range(8):
        if (sor + oszlop) % 2 == 0:
            sor_str += "*"
        else:
            sor_str += " "
    print(sor_str)


print("------ 5. ------")
start = safeInput("Add meg az első számot: ")
stop = safeInput("Add meg a második számot: ")
lepes = safeInput("Add meg a lépésközt (pozitív): ", int, 1)
if start <= stop:
    for i in range(start, stop + 1, lepes):
        print(i, end=" ")
else:
    for i in range(start, stop - 1, -lepes):
        print(i, end=" ")
print()


print("------ 6. ------")
n_bev = safeInput("Add meg n értékét: ", int, 1)
negyz_s = ""
for i in range(1, n_bev + 1):
    if i == n_bev:
        negyz_s += f"{i**2}"
    else:
        negyz_s += f"{i**2};"
print(negyz_s)


print("------ 7. ------")
n_kob = safeInput("Add meg n értékét: ", int, 1)
for i in range(1, n_kob + 1):
    print(f"{i} köbe = {i**3}")


print("------ 8. ------")
a_bev = safeInput("Add meg 'a' értékét: ")
b_bev = safeInput("Add meg 'b' értékét: ")
min_v = min(a_bev, b_bev)
max_v = max(a_bev, b_bev)
for i in range(min_v, max_v + 1):
    if i >= 0:
        print(f"sqrt({i}) = {sqrt(i):.2f}")
    else:
        print(f"sqrt({i}) = nem értelmezett")


print("------ 9. ------")
fakt_n = safeInput("Add meg n-t a faktoriálishoz: ", int, 1)
fakt = 1
for i in range(1, fakt_n + 1):
    fakt *= i
print(f"{fakt_n}! = {fakt}")


print("------ 10. ------")
n_negyzet = safeInput("Add meg n értékét az első n négyzetszámhoz: ", int, 1)
for i in range(1, n_negyzet + 1):
    print(f"{i}. négyzetszám: {i**2}")


print("------ 11. ------")
n_paratlan = safeInput("Add meg N-t a páratlan számok összegéhez: ", int, 1)
paratlan_osszeg = sum(i for i in range(1, n_paratlan + 1, 2))
print(f"Az N-nél nem nagyobb páratlan számok összege: {paratlan_osszeg}")


print("------ 12. ------")
k_szam = safeInput("Add meg K pozitív egész számot: ", int, 1)
sorozat_osszeg = 0
for i in range(1, k_szam + 1):
    sorozat_osszeg += i * (i + 1)
print(f"A sorozat összege 1*2-től {k_szam}*({k_szam}+1)-ig: {sorozat_osszeg}")


print("------ 13. ------")
n_tobb = safeInput("Add meg N természetes számot: ", int, 1)
print(f"A 3 többszörösei {n_tobb}-ig:")
for i in range(3, n_tobb + 1, 3):
    print(i, end=" ")
print()


print("------ 14. ------")
n_fib = safeInput("Add meg az első N Fibonacci számot: ", int, 1)
if n_fib > 0:
    a, b = 0, 1
    fib_list = []
    for _ in range(n_fib):
        fib_list.append(a)
        a, b = b, a + b
    print("Fibonacci számok:", fib_list)


print("------ 15. ------")
n_prim = safeInput("Add meg az első N prímszámot: ", int, 1)
primes = []
current = 2
while len(primes) < n_prim:
    is_p = True
    for p in primes:
        if p * p > current:
            break
        if current % p == 0:
            is_p = False
            break
    if is_p:
        primes.append(current)
    current += 1
print("Prímszámok:", primes)


print("------ 16. ------")
print("Szorzótábla (1-3):")
for i in range(1, 4):
    row_str = f"{i} "
    for j in range(1, 4):
        row_str += f"{i*j:3}"
    print(row_str)


print("------ 17. ------")
print("10 véletlen szám különböző intervallumokból:")
print("[0,10]:", [random.randint(0, 10) for _ in range(10)])
print("[0,25]:", [random.randint(0, 25) for _ in range(10)])
print("[0,50]:", [random.randint(0, 50) for _ in range(10)])
print("[10,75]:", [random.randint(10, 75) for _ in range(10)])
print("[-50,50]:", [random.randint(-50, 50) for _ in range(10)])
print("[-100,-70]:", [random.randint(-100, -70) for _ in range(10)])


print("------ 18. ------")
csillag_db = safeInput("Adj meg egy egész számot a csillagokhoz: ", int, 1)
print("*" * csillag_db)
print("Négyzet rajzolása:")
for _ in range(csillag_db):
    print("*" * csillag_db)


print("------ 19. ------")
m_sz = safeInput("Add meg M-et (szélesség): ", int, 1)
n_mag = safeInput("Add meg N-et (magasság): ", int, 1)
for _ in range(n_mag):
    print("*" * m_sz)


print("------ 20. ------")
m_par = safeInput("Add meg M-et (szélesség): ", int, 1)
n_par = safeInput("Add meg N-et (sorok száma): ", int, 1)
for _ in range(n_par):
    print("*" * m_par)


print("------ 21. ------")
n_harom = safeInput("Add meg a háromszög magasságát (N): ", int, 1)
for i in range(1, n_harom + 1):
    print("*" * (2 * i - 1))


print("------ 22. ------")
m_uk = safeInput("Add meg M-et (szélesség): ", int, 1)
n_uk = safeInput("Add meg N-et (magasság): ", int, 1)
for i in range(n_uk):
    if i == 0 or i == n_uk - 1:
        print("*" * m_uk)
    else:
        if m_uk > 2:
            print("*" + " " * (m_uk - 2) + "*")
        else:
            print("*" * m_uk)


print("------ 23. ------")
feladat_db = safeInput("Hány feladatot szeretnél megoldani? ", int, 1)
helyes = 0
for _ in range(feladat_db):
    a_rnd = random.randint(1, 100)
    b_rnd = random.randint(1, 100)
    print(f"\nSzámok: {a_rnd} és {b_rnd}")
    user_osszeg = safeInput("Mennyi a két szám összege? ")
    user_kulonbseg = safeInput("Mennyi a két szám különbsége? ")

    valos_osszeg = a_rnd + b_rnd
    valos_kulonbseg = a_rnd - b_rnd

    if user_osszeg == valos_osszeg and user_kulonbseg == valos_kulonbseg:
        print("Jó eredmény!")
        helyes += 1
    else:
        print(
            f"Rossz eredmény! A helyes összeg: {valos_osszeg}, a különbség: {valos_kulonbseg}"
        )
print(
    f"\nEredmény: {helyes}/{feladat_db} helyes válasz ({helyes/feladat_db*100:.1f}%)"
)


print("------ 24. ------")
print("Kód\tKarakter")
for code in range(32, 256):
    print(f"{code}\t{chr(code)}")


print("------ 25. ------")
poz_szam = safeInput("Adjon meg egy pozitív egész számot az osztókhoz: ", int, 1)
print(f"A(z) {poz_szam} osztói:")
for i in range(1, poz_szam + 1):
    if poz_szam % i == 0:
        print(i, end=" ")
print()


print("------ 26. ------")
poz_szam2 = safeInput(
    "Adjon meg egy pozitív egész számot az osztók összegéhez: ", int, 1
)
osztok_osszege = sum(i for i in range(1, poz_szam2 + 1) if poz_szam2 % i == 0)
print(f"Az osztók összege: {osztok_osszege}")


print("------ 27. ------")
tok_szam = safeInput(
    "Adjon meg egy pozitív egész számot a tökéletes szám vizsgálathoz: ", int, 1
)
div_sum = sum(i for i in range(1, tok_szam + 1) if tok_szam % i == 0)
if div_sum == 2 * tok_szam:
    print(f"A(z) {tok_szam} egy TÖKÉLETES szám.")
else:
    print(f"A(z) {tok_szam} nem tökéletes szám.")


print("------ 28. ------")
alap = safeInput("Hatványalap: ", float)
kitevo = safeInput("Kitevő: ", int)
eredmeny = 1
for _ in range(abs(kitevo)):
    eredmeny *= alap
if kitevo < 0:
    eredmeny = 1 / eredmeny
print(f"A Hatványérték: {eredmeny}")


print("------ 29. ------")
print("Vigenère-tábla:")
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(abc)):
    sor = abc[i:] + abc[:i]
    print(sor)