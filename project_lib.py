import json  # Importing JSON module for saving and loading books

# List to store books
library = []

def add_book():
    """Function to add a book to the library."""
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = int(input("Enter publication year: "))  # Convert input to integer
    genre = input("Enter genre: ")
    read_status = input("Have you read it? (yes/no): ").strip().lower() == "yes"  # Convert input to boolean
    
    # Creating a dictionary to store book details
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)  # Adding book to the list
    print(f'"{title}" added successfully!\n')

def remove_book():
    """Function to remove a book by title."""
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f'"{title}" removed successfully!\n')
            return
    print("Book not found!\n")

def search_book():
    """Function to search for books by title or author."""
    keyword = input("Enter book title or author to search: ").lower()
    results = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower()]
    if results:
        for book in results:
            print(f'{book["title"]} by {book["author"]} ({book["year"]}) - {"Read" if book["read"] else "Unread"}')
    else:
        print("No matching books found!\n")

def display_books():
    """Function to display all books in the library."""
    if not library:
        print("No books in the library!\n")
        return
    print("\nYour Library:")
    for book in library:
        print(f'{book["title"]} by {book["author"]} ({book["year"]}) - {"Read" if book["read"] else "Unread"}')
    print()

def display_statistics():
    """Function to show total books and percentage read."""
    total_books = len(library)
    if total_books == 0:
        print("No books in the library!\n")
        return
    read_books = sum(book["read"] for book in library)  # Counting read books
    print(f"Total Books: {total_books}")
    print(f"Books Read: {read_books} ({(read_books / total_books) * 100:.2f}% read)\n")

def save_library():
    """Function to save the book list to a file."""
    with open("library.json", "w") as file:
        json.dump(library, file)  # Save list as JSON file

def load_library():
    """Function to load books from a file if it exists."""
    global library
    try:
        with open("library.json", "r") as file:
            library = json.load(file)
    except FileNotFoundError:
        library = []  # If file not found, start with an empty list

def main():
    """Main function to handle the menu system."""
    load_library()  # Load books when the program starts
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()  # Save books before exiting
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select again.\n")

if __name__ == "__main__":
    main()
