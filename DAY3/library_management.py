library = {}
def add_book(book_id, title):
    library[book_id] = title
def remove_book(book_id):
    library.pop(book_id, None)
def search_book(book_id):
    return library.get(book_id, "Book ID not found")
def update_book(book_id, new_title):
    if book_id in library:
        library[book_id] = new_title
def display_books():
    if library:
        for book_id, title in library.items():
            print(f"{book_id}: {title}")
    else:
        print("Library is empty")
def count_books():
    return len(library)
def check_title_exists(title):
    return title in library.values()
while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book by ID")
    print("4. Update Book Title")
    print("5. Display All Books")
    print("6. Count Total Books")
    print("7. Check if Book Title Exists")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")
    if choice == '1':
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        add_book(book_id, title)
        print("Book added successfully.")
    elif choice == '2':
        book_id = int(input("Enter Book ID to remove: "))
        remove_book(book_id)
        print("Book removed successfully (if it existed).")
    elif choice == '3':
        book_id = int(input("Enter Book ID to search: "))
        print("Book Title:", search_book(book_id))
    elif choice == '4':
        book_id = int(input("Enter Book ID to update: "))
        new_title = input("Enter new Book Title: ")
        update_book(book_id, new_title)
        print("Book updated successfully.")
    elif choice == '5':
        print("All books in library:")
        display_books()
    elif choice == '6':
        print("Total number of books:", count_books())
    elif choice == '7':
        title = input("Enter Book Title to check: ")
        if check_title_exists(title):
            print("Book exists in the library.")
        else:
            print("Book does not exist in the library.")
    elif choice == '8':
        print("Exiting Library Management System.")
        break
    else:
        print("Invalid choice. Please enter 1-8.")