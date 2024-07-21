#Kласс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
#Функции-члены реализуют запись и считывание полей (проверка корректности).
#Создать список объектов. Вывести:
#a)	список книг заданного автора;
#б) список книг, выпущенных после заданного года.

class Book:
    _id_autoincrement = 1

    def __init__(self, title, author, publishing_house, year_of_publishing, number_of_pages, price, binding_type):
        self.__id = Book._id_autoincrement        #id
        Book._id_autoincrement += 1
        self.__title = title                  #  название
        self.__author = author
        self.__publishing_house = publishing_house      # издательство
        self.__year_of_publishing = year_of_publishing
        self.__number_of_pages = number_of_pages         # количество страниц
        self.__price = price
        self.__binding_type = binding_type    # тип переплета

    # Сеттер метод, изменяющий значение закрытого атрибута для экземпляра класса
    def set_id(self, id):
        self.__id = id

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_year_of_publishin(self, year_of_publishing):
        if year_of_publishing > 2024:
            raise ValueError("Неверно указан год!!!")
        self.__year_of_publishing = year_of_publishing

    def set_publishing_house(self, publishing_house):
        self.__publishing_house = publishing_house

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages < 1:
            raise ValueError("Неверно указано количество страниц!!!")
        self.__number_of_pages = number_of_pages

    def set_price(self, price):
        if price < 1:
            raise ValueError("Неверно указана стоимость!!!")
        self.__price = price

    def set_binding_type(self, binding_type):
        self.__binding_type = binding_type

    # Геттер метод, возвращающий значение закрытого атрибута для экземпляра класса
    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publishing_house(self):
        return self.__publishing_house

    def year_of_publishing(self):
        return self.__year_of_publishing

    def get_number_of_pages(self):
        return self.__number_of_pages

    def get_price(self):
        return self.__price

    def get_binding_type(self):
        return self.__binding_type

    # метод вывода данных
    @staticmethod
    def printBookInfo(book):
        print(f"{book.__id}, "
            f"{book.__title}, "
            f"{book.__author}, "
            f"{book.__publishing_house}, "
            f"{book.__year_of_publishing}, "
            f"{book.__number_of_pages}, "
            f"{book.__price}, "
            f" {book.__binding_type}")

    # метод вывода списка книг заданного автора
    @classmethod
    def printBookAuthor(cls, bookList, authorBook):
        count = 0
        for i in range(len(bookList)):
            if authorBook == bookList[i].get_author():
                Book.printBookInfo(bookList[i])
                count += 1
        if count == 0:
            print("Автора " + authorBook + " нет!")

    # список книг, выпущенных после заданного года
    @classmethod
    def printBookYear(cls, bookList, year):
        count = 0
        for i in range(len(bookList)):
            if year >= bookList[i].get_year_of_publishing:
                Book.printBookInfo(bookList[i])
                count += 1
        if count == 0:
            print("книг " + str(year) + " г. - нет!")


bookList = []
count = int(input("Сколько книг будем вводить? "))

for i in range(count):
    title = input("Введите название: ")
    author = input("Введите автора: ")
    publishing_house = input("Введите издательство: ")
    year_of_publishing = int(input("Введите год издания: "))
    number_of_pages = input("Введите количество страниц: ")
    price = int(input("Введите стоимость: "))
    binding_type = input("Введите тип переплета: ")

    book = Book(title, author, publishing_house, year_of_publishing, number_of_pages, price, binding_type)
    bookList.append(book)

# вывод данных на экран
for i in range(len(bookList)):
    Book.printBookInfo(bookList[i])


print("\n*********************************************************************************************\n")
# Вывод списка книг заданного автора
authorBook = input("Введите автора книг для поиска: ")
print(f"\nКниги автора {authorBook}: ")
Book.printBookAuthor(bookList, authorBook)

print("\n*********************************************************************************************\n")
# Вывод списка книг, выпущенных после заданного года
year = int(input("введите год? "))
print(f"\nкниги после ({year}) года.: ")
Book.printBookYear(bookList, year)