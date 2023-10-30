#Клас бібліотеки та книги

class Book:
    def __init__(self, name, total_pages, pages_read):
        self.name = name
        self.total_pages = total_pages
        self.pages_read = pages_read

    def read_pages_percent(self):
        return (self.pages_read / self.total_pages) * 100.0

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Книги не знайдено.")

    def book_list(self):
        for i, book in enumerate(self.books):
            print(f"{i + 1}. Назва книги: {book.name}, Прочитано сторінок: {book.read_pages_percent():.1f}%")


Library = Library()

#Робота з книгами та бібліотекою

while True:
    #Вибір запропонованих команд
    main_input = input("Для продовження виберіть одну з команд: "
                        "\n1) Додати книгу"
                        "\n2) Видалити книгу" 
                        "\n3) Записи книги " 
                        "\n4) Завершення програми " 
                        "\n Введіть номер обраної команди ")

    if main_input == "1":
        name = input("Введіть назву книги, яку ви бажаєте додати: ")
        while True:
            try:
                total_pages = int(input("Введіть кількість сторінок у книзі "))
                pages_read = int(input("Введіть кількість прочитаних сторінок у книзі "))
                if total_pages >= pages_read:
                    new_book = Book(name, total_pages, pages_read)
                    Library.add_book(new_book)
                    print("Книгу було додано до бібліотеки")
                    break
                else:
                    print("В книзі не може бути прочитано більше сторінок ніж зазначено. \nВведіть кількість сторінок ще раз: ")
            except ValueError:
                print("Невірний формат вводу. Введіть число.")

    if main_input == "2":
        Library.book_list()
        book_num = int(input("Введіть номер книги яку бажаєте видалити: "))
        if 1 <= book_num <= len(Library.books):
            delete_book = Library.books[book_num - 1]
            Library.remove_book(delete_book)
            print(f"Книга {book_num} була видалена")
        else:
            print("Книги з таким номером не існує")

    if main_input == "3":
        Library.book_list()

    if main_input == "4":
        break