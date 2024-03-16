books = []

def add_book(title,author,year,books):
    book = {"title" : title,
            "author": author,
            "year":year}
    books.append(book)

def display(books):
    for book in books:
        print(book)

while True:
    print("1.add book")
    print("2.display book")
    print("3.exit")
    choice = input("enter your choice")

    if choice == "1":
        title = input("enter the title of ur book")
        author = input("enter the author of the book")
        year = input("enter the year of the book")
        add_book(title,author,year,books)
        print("added")
    elif choice == "2":
        display(books)
    elif choice  == "3":
        print("exiting...")
        break
    else:
        print("invalid choice.. please try again")

