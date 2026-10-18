import random


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


def feladat1():
    print("------ 1. Feladat ------")
    kezdotoke = safeInput("Adja meg a kezdőtőkét (Ft): ", float, 1)
    kamat = safeInput("Adja meg az éves kamatlábat (%): ", float, 1)
    cel = 300000
    ev = 0

    while kezdotoke < cel:
        kezdotoke *= 1 + (kamat / 100)
        ev += 1

    print(f"A tőke {ev} év után éri el a {cel} Ft-ot.")
    print(f"Végösszeg: {kezdotoke:.0f} Ft")


def feladat2():
    print("------ 2. Feladat ------")
    magassag = safeInput("Adja meg a labda kezdeti magasságát (m): ", float, 1)
    pattanas = 0

    while magassag > 0.2:
        magassag *= 0.5
        pattanas += 1

    print(f"A labda {pattanas} pattanás után lesz kisebb, mint 0,2 m.")


def feladat3():
    print("------ 3. Feladat ------")
    szam = safeInput("Adja meg a számot: ", int, 1)
    lepes = 0

    while szam != 1:
        print(szam, end=" ")
        if szam % 2 == 0:
            szam //= 2
        else:
            szam = szam * 3 + 1
        lepes += 1

    print(1)
    print(f"A sorozat {lepes} lépésből állt.")


def feladat4():
    print("------ 4. Feladat ------")
    hatar = safeInput("Adja meg a felső határt: ", int, 1)
    ertek = 1

    while ertek * 2 <= hatar:
        ertek *= 2

    print(f"A legnagyobb kettő hatvány: {ertek}")


def feladat5():
    print("------ 5. Feladat ------")
    osszeg = 0
    db = 0

    while osszeg < 500:
        szam = safeInput("Adja meg a számot: ", int)
        osszeg += szam
        db += 1

    print(f"A végösszeg: {osszeg} Ft")
    print(f"{db} darab szám összegzése után értük el a 500-at.")


def feladat6():
    print("------ 6. Feladat ------")
    jelszo = "titok123"
    probalkozas = 0

    while True:
        bekert = input("Adja meg a jelszót: ")
        probalkozas += 1

        if bekert == jelszo:
            print("Sikeres belépés!")
            print(f"{probalkozas} próbálkozásból sikerült.")
            break
        else:
            print("Hibás jelszó, próbáld újra!")


def feladat7():
    print("------ 7. Feladat ------")
    while True:
        szo = input("Adja meg a szót: ")

        if szo == "stopp" or szo == ".":
            print("Viszlát!")
            break
        else:
            print(szo.upper())


def feladat8():
    print("------ 8. Feladat ------")
    while True:
        kor = safeInput("Adja meg az életkorát: ", int)

        if 0 <= kor <= 120:
            print(f"Köszönöm, az életkorod: {kor}")
            if kor > 99:
                print("A korod túl magas ahhoz, hogy a kirakós játékban részt vegyél.")
            break
        else:
            print("Hibás életkor, próbáld újra!")


def feladat9():
    print("------ 9. Feladat ------")
    osszeg = safeInput("Adja meg az összeget (Ft): ", int, 1)
    penz = [200, 100, 50, 20, 10, 5]
    db = {}

    for cimlet in penz:
        db[cimlet] = osszeg // cimlet
        osszeg %= cimlet

    print("Címletbontás:")
    for cimlet in penz:
        if db[cimlet] > 0:
            print(f"{cimlet} Ft: {db[cimlet]} db")


def feladat10():
    print("------ 10. Feladat ------")
    ido = safeInput("Adja meg a visszaszámlálás kezdőértékét: ", int, 1)

    while ido >= 0:
        print(ido)
        ido -= 1

    print("Kilövés!")


def feladat11():
    print("------ 11. Feladat ------")
    osszeg = 0
    db = 0

    while True:
        ar = safeInput("Adja meg a termék árát (0 = kilépés): ", int)
        if ar == 0:
            break
        osszeg += ar
        db += 1

    print(f"A termékek darabszáma: {db}")
    print(f"A végösszeg: {osszeg} Ft")


def feladat12():
    print("------ 12. Feladat ------")
    bakteriak = 100
    ora = 0

    while bakteriak < 50000:
        bakteriak *= 2
        ora += 1

    print(f"{ora} óra múlva éri el vagy haladja meg az 50 000 baktériumot.")


def feladat13():
    print("------ 13. Feladat ------")
    jelszo = "1234"

    for i in range(3):
        bekert = input("Adja meg a kódot: ")

        if bekert == jelszo:
            print("Belépés engedélyezve!")
            break
        else:
            print("Hibás kód!")

    else:
        print("Letiltva!")


def feladat14():
    print("------ 14. Feladat ------")
    dobasok = 0

    while True:
        dobasok += 1
        dobas = random.randint(1, 6)
        print(f"{dobasok}. dobás: {dobas}")

        if dobas == 6:
            print(f"A hatost a(z) {dobasok}. dobásnál dobtad.")
            break


def feladat15():
    print("------ 15. Feladat ------")
    while True:
        jegy = safeInput("Adja meg az érdemjegyet (1-5): ", int)

        if 1 <= jegy <= 5:
            print("Köszönöm, a jegyedet rögzítettem.")
            break
        else:
            print("Hibás érdemjegy, próbáld újra!")


def feladat16():
    print("------ 16. Feladat ------")
    osszeg = 0
    nap = 0

    while osszeg < 1000:
        nap += 1
        beletesz = safeInput(f"{nap}. nap: mennyi pénzt teszel a perselybe (Ft)? ", int, 1)
        osszeg += beletesz

    print(f"{nap} nap alatt gyűlt össze a pénz.")
    print(f"A végösszeg: {osszeg} Ft")


def feladat17():
    print("------ 17. Feladat ------")
    szam = safeInput("Adja meg a számot: ", int, 1)
    oszto = 2

    while szam % oszto != 0:
        oszto += 1

    print(f"A legkisebb 1-nél nagyobb osztó: {oszto}")


def feladat18():
    print("------ 18. Feladat ------")
    while True:
        print("[1] Új játék")
        print("[2] Segítség")
        print("[3] Kilépés")
        valasztas = safeInput("Válassz menüpontot: ", int)

        if valasztas == 1:
            print("Új játék indítása.")
        elif valasztas == 2:
            print("Segítség: válassz 1-et vagy 3-at.")
        elif valasztas == 3:
            print("Viszlát!")
            break
        else:
            print("Érvénytelen menüpont!")


def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()
    feladat8()
    feladat9()
    feladat10()
    feladat11()
    feladat12()
    feladat13()
    feladat14()
    feladat15()
    feladat16()
    feladat17()
    feladat18()


if __name__ == "__main__":
    main()
