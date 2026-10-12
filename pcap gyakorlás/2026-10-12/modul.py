class Book:
    def __init__(self, titel:str, author:str, year:int, taken:bool):
        self.titel = titel
        self.author = author
        self.year = year
        self.taken = taken

        self.data = {"title": self.titel, "author":self.author, "year":self.year, "taken":self.taken}

    def _update(self):
        self.titel = self.data["titel"]
        self.author = self.data["author"]
        self.year = self.data["year"]
        self.taken = self.data["taken"]
        
    def getData(self):
        return self.data

    def editData(self, property, value):
        self.data[property] = value
        self._update()

    def takeout(self):
        if self.taken:
            print("The book is already taken out")
            return False
        print("""Done
        The Book is taked out from now""")
        return True

    def back(self):
        if not self.taken:
            print("The book is not taken out")
            return False
        print("""Done
        The Book is returned from now""") 
        return True

#temp = Book("Neuromancer", "William Gibson", 1984, False)

class Libary:
    def __init__(self):
        self.data = {}
        self.nextId = 0
    
    def addBook(self, titel:str, author:str, year:int, taken:bool, Id:int=-1,):
        if Id == -1:
            while self.nextId in self.data.keys():
                self.nextId += 1
            self.data[self.nextId] = Book(titel, author, year, taken)
            self.nextId += 1
            return True
        elif Id < 0:
            return False
        else:
            self.data[Id] = Book(titel, author, year, taken)
            return True

    def getData(self):
        return self.data

    def edit(self, id, property, value):
        self.data[id].editData(property, value)

    def takeoutBook(self, id):
        self.data[id].takeout()

    def returnBook(self, id):
        self.data[id].back()

    def valiableBook(self):
        temp = self.data[:]
        ls = list(temp.keys())[:]
        for key in ls:
            if not temp[key].getData["taken"]:
                del(temp[key])
        return temp
