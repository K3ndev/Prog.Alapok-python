## 🐍 PCPP1 – 15 kérdéses gyakorlóteszt

 **Egy kérdésnél egy helyes válasz van. A megoldókulcsot most nem adom meg.**

 ### 1\. `@property`

 Mi lesz a kimenet?

```
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

p = Person(25)
print(p.age)
```

 A) `<property object>`\
 B) `25`\
 C) `_age`\
 D) Hiba történik

---

 ### 2\. Öröklődés és `super()`

 Mi lesz a kimenet?

```
class A:
    def __init__(self):
        self.x = 10

class B(A):
    def __init__(self):
        super().__init__()
        self.x += 5

obj = B()
print(obj.x)
```

 A) `10`\
 B) `5`\
 C) `15`\
 D) Hiba történik

---

 ### 3\. `__str__()`

 Mi lesz a kimenet?

```
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

p = Person("Anna")
print(p)
```

 A) `Anna`\
 B) `Person: Anna`\
 C) `<Person object>`\
 D) Hiba történik

---

 ### 4\. Osztályváltozó vs. példányváltozó

 Mi lesz a kimenet?

```
class Counter:
    value = 0

    def __init__(self):
        Counter.value += 1

a = Counter()
b = Counter()
c = Counter()

print(Counter.value)
```

 A) `0`\
 B) `1`\
 C) `2`\
 D) `3`

---

 ### 5\. `classmethod`

 Melyik állítás igaz?

```
class Person:
    count = 0

    @classmethod
    def increase(cls):
        cls.count += 1
```

 A) Az `increase()` csak példányon keresztül hívható.\
 B) A `cls` az aktuális példányt jelenti.\
 C) A `cls` az osztályra hivatkozik.\
 D) A `classmethod` nem módosíthat osztályváltozót.

---

 ### 6\. Dekorátor

 Mi lesz a kimenet?

```
def decorator(func):
    def wrapper():
        print("A")
        func()
        print("B")
    return wrapper

@decorator
def hello():
    print("Hello")

hello()
```

 A)

```
Hello
A
B
```

 B)

```
A
B
Hello
```

 C)

```
A
Hello
B
```

 D)

```
Hello
```

---

 ### 7\. Generátor

 Mi történik?

```
def numbers():
    yield 1
    yield 2
    yield 3

x = numbers()

print(next(x))
print(next(x))
```

 A)

```
1
2
```

 B)

```
2
3
```

 C)

```
1
3
```

 D) A `yield` miatt hibát kapunk.

---

 ### 8\. Closure

 Mi lesz a kimenet?

```
def outer(x):
    def inner():
        return x * 2
    return inner

func = outer(5)

print(func())
```

 A) `5`\
 B) `7`\
 C) `10`\
 D) Hiba történik

---

 ### 9\. `*args`

 Mi lesz a kimenet?

```
def calculate(*args):
    return sum(args)

print(calculate(1, 2, 3, 4))
```

 A) `4`\
 B) `10`\
 C) `(1, 2, 3, 4)`\
 D) Hiba történik

---

 ### 10\. `**kwargs`

 Mi lesz a `kwargs` típusa?

```
def test(**kwargs):
    print(type(kwargs))

test(name="Anna", age=25)
```

 A) `list`\
 B) `tuple`\
 C) `set`\
 D) `dict`

---

 ### 11\. Reguláris kifejezések

 Melyik minta illeszkedik egy olyan szövegre, amely **egy vagy több számjegyből áll**?

 A) `[a-z]+`\
 B) `\d+`\
 C) `\w*`\
 D) `.+`

---

 ### 12\. Fájlkezelés

 Miért előnyös az alábbi megoldás?

```
with open("data.txt", "r") as file:
    content = file.read()
```

 A) Automatikusan bezárja a fájlt.\
 B) Automatikusan törli a fájlt.\
 C) Csak bináris fájlokhoz használható.\
 D) Nem szükséges hozzá fájl.

---

 ### 13\. Kivételkezelés

 Mi lesz a kimenet?

```
try:
    print(10 / 0)
except ZeroDivisionError:
    print("A")
except Exception:
    print("B")
finally:
    print("C")
```

 A)

```
A
C
```

 B)

```
B
C
```

 C)

```
A
```

 D)

```
C
```

---

 ### 14\. Absztrakt osztályok

 Mire szolgál elsősorban az `ABC` és az `@abstractmethod`?

 A) A program gyorsítására.\
 B) Kötelezően megvalósítandó metódusok definiálására az utódosztályok számára.\
 C) Automatikus példányosításra.\
 D) Dictionary-k létrehozására.

---

 ### 15\. ⭐ Komplex PCPP1 kérdés

 Mi lesz a kimenet?

```
class A:
    def __init__(self):
        self.value = 10

    def get_value(self):
        return self.value

class B(A):
    def __init__(self):
        super().__init__()
        self.value += 5

    def get_value(self):
        return self.value * 2

obj = B()

print(obj.get_value())
print(obj.value)
```

 A)

```
15
15
```

 B)

```
30
15
```

 C)

```
20
10
```

 D)

```
30
10
```

---

 ## 📝 Válaszlap

 Írd vissza például így:

```
1. B
2. C
3. B
4. D
...
15. B
```