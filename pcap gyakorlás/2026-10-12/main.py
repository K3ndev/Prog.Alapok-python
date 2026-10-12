from modul import Book, Libary

lib = Libary()
isRunning = True

print("""
Könyvnapló v1

""")

commandSet = {
    "reg" : lambda title, author, year, taken, id = -1: lib.addBook(title, author, year, taken, id)
    ""
}

while isRunning:
    command = input("-> ")
    scliced = command.split(" ")
    if scliced[0]