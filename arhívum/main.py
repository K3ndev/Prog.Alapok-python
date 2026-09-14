
print("----- 1. Feladat -----")
nev = input("Mi a neve? ")
ev = int(input("Mikor született"))
print(f"Kendes {nev}! {ev}-ben születtél!")
kor = 2026 - ev
print(f"Kendes {nev}! {kor} éves vagy!")

print("----- 2. Feladat -----")

print("*" * (len(nev) + 4))
print(f"* {nev} *")
print("*" * (len(nev) + 4))