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


print("------ 21. ------")
pont = safeInput("Adja meg a dolgozat pontszámát (0-100): ", int, 1)
if 0 <= pont <= 42:
    print("Értékelés: elégtelen (1)")
elif 43 <= pont <= 57:
    print("Értékelés: elégséges (2)")
elif 58 <= pont <= 72:
    print("Értékelés: közepes (3)")
elif 73 <= pont <= 87:
    print("Értékelés: jó (4)")
elif 88 <= pont <= 100:
    print("Értékelés: jeles (5)")
else:
    print("Hibás pontszám! (0-100 között kell lennie)")


print("------ 22. ------")
kor = safeInput("Adja meg az életkorát: ", int, 1)
if 0 <= kor <= 13:
    print("Kategória: Gyerek")
elif 14 <= kor <= 17:
    print("Kategória: Fiatalkorú")
elif 18 <= kor <= 23:
    print("Kategória: Ifjú")
elif 24 <= kor <= 59:
    print("Kategória: Felnőtt")
else:
    print("Kategória: Idős")


print("------ 23. ------")
targy_suruseg = safeInput("Adja meg a tárgy sűrűségét: ", float, 1)
folyadek_suruseg = safeInput("Adja meg a folyadék sűrűségét: ", float, 1)

if targy_suruseg > folyadek_suruseg:
    print("A tárgy elmerül.")
elif folyadek_suruseg > targy_suruseg:
    print("A tárgy úszik.")
else:
    print("A tárgy lebeg.")


print("------ 24. ------")
hianyzas = safeInput(
    "Adja meg az igazolatlan hiányzások számát: ", int, 1
)
if hianyzas == 0:
    print("Magatartás jegy: 5 (példás)")
elif 1 <= hianyzas <= 3:
    print("Magatartás jegy: 4 (jó)")
elif 4 <= hianyzas <= 9:
    print("Magatartás jegy: 3 (változó)")
else:
    print("Magatartás jegy: 2 (rossz)")
    szul_ev = safeInput("Adja meg a tanuló születési évét: ", int, 1)
    # Feltételezve a naptári évet (2026)
    if 2026 - szul_ev < 18:
        print("Szülői értesítés szükséges")
    else:
        print("Felszólítás kiküldése szükséges")

print("------ 26. ------")
v = safeInput("Adja meg az autó sebességét (km/h): ", float, 1)
if 0 <= v <= 1:
    print("Hasonló állat: Csiga (0-1 km/h)")
elif 1 < v <= 6:
    print("Hasonló állat: Csuka (1-6 km/h)")
elif 6 < v <= 32:
    print("Hasonló állat: Bálna (7-32 km/h)")
elif 32 < v <= 48:
    print("Hasonló állat: Ezüst sirály (32-48 km/h)")
elif 48 < v <= 64:
    print("Hasonló állat: Nyúl (48-64 km/h)")
elif 64 < v <= 70:
    print("Hasonló állat: Strucc (65-70 km/h)")
elif 70 < v <= 110:
    print("Hasonló állat: Gepárd (71-110 km/h)")
elif 110 < v <= 320:
    print("Hasonló állat: Vadászsólyom zuhanórepülésben (111-320 km/h)")
else:
    print("Ennyivel még a vadászsólyom sem repül!")


print("------ 27. ------")
d = safeInput("Adja meg a távolságot (km): ", float, 1)
if 1 <= d <= 2:
    print("Díjazás: 500 Ft")
elif 3 <= d <= 5:
    print("Díjazás: 700 Ft")
elif 6 <= d <= 10:
    print("Díjazás: 900 Ft")
elif 11 <= d <= 20:
    print("Díjazás: 1 400 Ft")
elif 21 <= d <= 30:
    print("Díjazás: 2 000 Ft")
else:
    print("Erre a távolságra nincs egyedi díjszabás meghatározva.")


print("------ 28. ------")
szelesseg = safeInput("Adja meg a telek szélességét (m): ", float, 1)
hosszusag = safeInput("Adja meg a telek hosszúságát (m): ", float, 1)
alap_ado = safeInput("Adja meg az alap telekadót (Ft): ", float, 1)

if szelesseg <= 15 or hosszusag <= 25:
    korrigalt_ado = alap_ado * 0.8
    print(f"20% adókedvezmény jár! A fizetendő adó: {korrigalt_ado} Ft")
else:
    print(f"Nem jár kedvezmény. A fizetendő adó: {alap_ado} Ft")


print("------ 29. ------")
T = safeInput("Adjon meg egy évszámot (1800-2099): ", int, 1)
if 1800 <= T <= 2099:
    A = T % 19
    B = T % 4
    C = T % 7
    D = (19 * A + 24) % 30
    E = (2 * B + 4 * C + 6 * D + 5) % 7

    H = 22 + D + E

    if E == 6 and D == 29:
        H = 50
    elif E == 6 and D == 28 and A > 10:
        H = 49

    if H <= 31:
        print(f"Húsvét vasárnap dátuma: március {H}.")
    else:
        print(f"Húsvét vasárnap dátuma: április {H - 31}.")
else:
    print("A megadott évszám kívül esik a [1800, 2099] intervallumon.")


print("------ 30. ------")
jegy = safeInput("Adja meg az érdemjegyet (1-5): ", int, 1)
if jegy == 1:
    print("Elégtelen")
elif jegy == 2:
    print("Elégséges")
elif jegy == 3:
    print("Közepes")
elif jegy == 4:
    print("Jó")
elif jegy == 5:
    print("Jeles")
else:
    print("Nincs ilyen érdemjegy!")


print("------ 31. ------")
nap_szam = safeInput("Adja meg a hét napjának sorszámát (1-7): ", int, 1)
napok = [
    "Hétfő",
    "Kedd",
    "Szerda",
    "Csütörtök",
    "Péntek",
    "Szombat",
    "Vasárnap",
]
if 1 <= nap_szam <= 7:
    print(f"A nap neve: {napok[nap_szam - 1]}")
else:
    print("Nincs ilyen nap a héten!")


print("------ 32. ------")
ev = safeInput("Adja meg az évet: ", int, 1)
honap = safeInput("Adja meg a hónap sorszámát (1-12): ", int, 1)
nap = safeInput("Adja meg a napot: ", int, 1)

honapok = [
    "január",
    "február",
    "március",
    "április",
    "május",
    "június",
    "július",
    "augusztus",
    "szeptember",
    "október",
    "november",
    "december",
]
if 1 <= honap <= 12:
    print(f"Dátum: {ev}. {honapok[honap - 1]} {nap}.")
else:
    print("Érvénytelen hónap!")


print("------ 33. ------")
kocka = random.randint(1, 6)
print(f"A dobás értéke: {kocka}")
if kocka in [1, 2]:
    print("Gyenge!")
elif kocka in [3, 4]:
    print("Nem rossz!")
elif kocka == 5:
    print("Jó!")
elif kocka == 6:
    print("Kiváló!")


print("------ 34. ------")
print(f"a) 0..100: {random.randint(0, 100)}")
print(f"b) -100..0: {random.randint(-100, 0)}")
print(f"c) 10..90: {random.randint(10, 90)}")
print(f"d) -100..100: {random.randint(-100, 100)}")
print(f"e) -50..50: {random.randint(-50, 50)}")
print(f"f) 1000..2000: {random.randint(1000, 2000)}")
print(f"g) 8000..150000: {random.randint(8000, 150000)}")


print("------ 35. ------")
lab = safeInput("Adja meg a hosszúságot lábban: ", float, 1)
huvelyk = safeInput("Adja meg a hosszúságot hüvelykben: ", float, 1)
cm = lab * 30.48 + huvelyk * 2.54
print(f"A megadott hosszúság centiméterben: {cm:.2f} cm")


print("------ 36. ------")
gallon = safeInput("Adja meg a víz mennyiségét gallonban: ", float, 1)
liter = gallon * 4.543
tomeg_kg = liter * 0.998
tomeg_dkg = tomeg_kg * 100
font = tomeg_dkg / 45.36
print(f"{gallon} gallon víz tömege kb. {font:.2f} font.")


print("------ 37. ------")
d_nap = safeInput("Adja meg a hónap hányadik napja van (1-31): ", int, 1)
d_ora = safeInput("Adja meg a jelenlegi órát (0-23): ", int)
ora_osszesen = (d_nap - 1) * 24 + d_ora
print(f"A hónap {ora_osszesen}. órájában vagyunk.")


print("------ 38. ------")
valasztas = safeInput(
    "Mit szeretne váltani? (1: fok -> radián, 2: radián -> fok): "
)
if valasztas == 1:
    fok = safeInput("Adja meg a szöget fokban: ", float)
    rad = fok * (3.141592653589793 / 180)
    print(f"{fok}° = {rad:.4f} rad")
elif valasztas == 2:
    rad = safeInput("Adja meg a szöget radiánban: ", float)
    fok = rad * (180 / 3.141592653589793)
    print(f"{rad} rad = {fok:.2f}°")


print("------ 39. ------")
f_num = safeInput("Adjon meg egy valós számot: ", float)
print(f"A szám abszolút értéke: {abs(f_num)}")