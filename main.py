# main.py
from library import Library

def main():
    lib = Library()
    role = input("Are you an Admin or Student? ").strip().lower()

    while True:
        if role == "admin":
            print("\n=== Admin Menu ===")
            print("1. Add Book")
            print("2. Display Available Books")
            print("3. Delete Book")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Book title: ")
                author = input("Author: ")
                lib.add_book(title, author)

            elif choice == "2":
                lib.display_books()

            elif choice == "3":
                title = input("Book title to delete: ")
                lib.delete_book(title)

            elif choice == "4":
                print("Exiting Admin Menu. Bye!")
                break

        elif role == "student":
            print("\n=== Student Menu ===")
            print("1. Display Books")
            print("2. Lend Book")
            print("3. Return Book")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                lib.display_books()

            elif choice == "2":
                title = input("Book title to borrow: ")
                lib.lend_book(title)

            elif choice == "3":
                title = input("Book title to return: ")
                lib.return_book(title)

            elif choice == "4":
                print("Exiting Student Menu. Bye!!")
                break
if __name__ == "__main__":
    main()
    
     


        

