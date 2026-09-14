🐍 PCAP Python gyakorlófeladat – Vizsgaeredmények
Feladat

Írj egy Python programot, amely egy vizsgázók eredményeit dolgozza fel.

A program kapja meg az alábbi adatokat:

results = {
    "Anna": [85, 92, 78],
    "Béla": [55, 61, 58],
    "Csilla": [95, 88, 91],
    "Dávid": [40, 52, 45],
    "Erika": [72, 75, 80]
}

1. Átlag számítása

Írj egy average() nevű függvényt, amely megkapja egy tanuló pontszámait tartalmazó listát, és visszaadja az átlagot.

2. Osztályzat meghatározása

Írj egy grade() nevű függvényt, amely az átlag alapján osztályzatot ad:

Átlag	Osztályzat
90–100	A
80–89	B
70–79	C
60–69	D
0–59	F
3. Eredmények kiírása

A program írja ki minden tanuló:

nevét,
átlagát,
osztályzatát.

Például:

Anna: 85.00 -> B
Béla: 58.00 -> F
Csilla: 91.33 -> A
Dávid: 45.67 -> F
Erika: 75.67 -> C

4. Sikeres vizsgázók

Számold meg, hány tanuló ment át.

Átmenő osztályzat:

A
B
C
D

Az F osztályzat sikertelen.

5. Legjobb eredmény

Írd ki a legjobb eredményt elérő tanuló nevét és átlagát.

Példa:

Legjobb eredmény: Csilla (91.33)

6. Összesítés

A program végén jelenjen meg:

Sikeresen teljesítette: 3 fő
Legjobb eredmény: Csilla (91.33)

⭐ Extra feladat

Készíts egy get_result(name) nevű függvényt.

A függvény:

kapja meg egy tanuló nevét paraméterként,
keresse meg a tanulót a results dictionary-ben,
számítsa ki az átlagát,
határozza meg az osztályzatát,
írja ki az eredményt.

Ha a megadott név nem létezik, kezeld a hibát KeyError segítségével.

Példa:

get_result("Anna")


Kimenet:

Anna: 85.00 -> B


Ismeretlen név esetén:

A megadott tanuló nem található.

📌 Megkötések

A megoldás során használd:

dictionary
list
for ciklus
if / elif / else
saját függvények
sum()
len()
try / except

Ne használj külső könyvtárakat.