#Skander Radhouane
# TP089787


from datetime import datetime  # Imports the datetime class from the datetime module to work with dates and times


# Global list to store all books
books = []


def calculate_overdue_fine(book):
    """
    Calculates the overdue fine for a given book.
    :param book: dictionary with keys 'borrow_date', 'due_date', 'returned', and optionally 'return_date'
    :return: fine amount in RM
    """
    fine = 0.0
    
    # ✅ If the fine is already paid, no calculation needed
    if book.get("fine_paid") is True:
        book["fine"] = 0.0
        return 0.0
    
    if book["returned"]:  
        # Book has been returned → check against return_date
        if book["return_date"] and book["return_date"] > book["due_date"]:
            overdue_days = (book["return_date"] - book["due_date"]).days
            fine = overdue_days * 0.80
    else:
        # Book not yet returned → check against today's date
        today = datetime.now()
        if today > book["due_date"]:
            overdue_days = (today - book["due_date"]).days
            fine = overdue_days * 0.80

    # Update fine in dictionary
    book["fine"] = fine
    return fine


def add_books():
    """
    Function to input one or more book details , after adding a book , the user will be asked to add another one ,if he/she writes "y",
    he/she will be able to add another one, otherwise he/she will exit the fuction.
    Each book will include title, borrower, borrow date, due date
    """
    while True:
        print("\n--- Add a New Book ---")
        
        # Input book details with validation
        title = input("Enter book title: ").strip()
        while not title:
            title = input("Book title cannot be empty. Enter book title: ").strip()
        
        borrower = input("Enter borrower name: ").strip()
        while not borrower:
            borrower = input("Borrower name cannot be empty. Enter borrower name: ").strip()
        
        # Validate dates
        while True:
            try:
                borrow_date = input("Enter borrow date (YYYY-MM-DD): ").strip()
                borrow_date = datetime.strptime(borrow_date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")
        
        while True:
            try:
                due_date = input("Enter due date (YYYY-MM-DD): ").strip()
                due_date = datetime.strptime(due_date, "%Y-%m-%d")
                if due_date < borrow_date:
                    print("Due date cannot be earlier than borrow date!")
                else:
                    break
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")
        
        # Ask if the book is returned
        return_date = None
        fine_paid = None
        while True:
            returned_input = input("Is the book returned? (y/n): ").strip().lower()
            if returned_input == "y":
                returned = True
                # Ask for return date
                while True:
                    try:
                        return_date = input("Enter return date (YYYY-MM-DD): ").strip()
                        return_date = datetime.strptime(return_date, "%Y-%m-%d")
                        if return_date < borrow_date:
                            print("❌ Return date cannot be earlier than borrow date!")
                        else:
                            break
                    except ValueError:
                        print("Invalid date format! Please use YYYY-MM-DD.")
                break
            elif returned_input == "n":
                returned = False
                break
            else:
                print("Invalid answer. Please choose 'y' or 'n'.")
        
        # Store details in a dictionary
        book = {
            "title": title,
            "borrower": borrower,
            "borrow_date": borrow_date,
            "due_date": due_date,
            "returned": returned,
            "return_date": return_date,
            "fine": 0.0,
            "fine_paid": None
        }
        # ✅ Then, only if returned late and fine > 0, ask if fine is paid
        if returned and return_date and return_date > due_date  :
            while True:
                fine_paid_input = input(f"Is the fine paid? (y/n): ").strip().lower() 
                if fine_paid_input == "y":
                    book["fine_paid"] = True
                    break
                elif fine_paid_input == "n":
                    book["fine_paid"] = False
                    break
                else:
                    print("Invalid answer. Please choose 'y' or 'n'.")
        # Function explained in overdue_fine.py
        book["fine"] = calculate_overdue_fine(book)
        # Add to global list
        books.append(book)
        print(f"✅ Book '{title}' added successfully!")
        
        # Ask if user wants to add another book
        count=0
        while True:
         count+=1
         another = input("Do you want to add another book? (y/n): ")
         # If the user enters 'y', break the loop (continue adding books)
         if another == 'y':
            break
         # If the user enters 'n', stop the process and exit the function
         elif another =='n':
             return
         else:
             # Allow up to 3 invalid attempts
             if(count<=3):
                 print("invalid answer. Please choose 'y' or 'n'")
             else:
                 # After 3 invalid attempts, exit automatically
                 print("invalid answer. Automatic exit")
                 return
             
             
def calculate_total_borrower_fine(books):
    """
    Function that calculates the total fine for a list of books borrowed by one borrower.
    Each book's overdue fine is calculated using the helper function `calculate_overdue_fine`.
    
    :param books: (list) list of book dictionaries belonging to the same borrower
    :return: (float) total fine amount
    """
    total_fine=0
    # Loop through each book in the borrower's list
    for book in books:
        # Add the overdue fine of the current book to the total
        total_fine += calculate_overdue_fine(book)
    return total_fine


def display_all_books(books):
    """
    Displays all books in the library with their details.
    :param books: (list) list of book dictionaries
    """
    if not books:
        print("\nNo books in the system yet.")
        return

    print("\n--- All Borrowed Books ---")
    for i, book in enumerate(books, start=1):
        print(f"\nBook {i}:")
        print(f"  Title       : {book['title']}")
        print(f"  Borrower    : {book['borrower']}")
        print(f"  Borrowed    : {book['borrow_date'].strftime('%Y-%m-%d')}")
        print(f"  Due Date    : {book['due_date'].strftime('%Y-%m-%d')}")
        print(f"  Returned    : {'Yes' if book['returned'] else 'No'}")

        # ✅ If returned, show return date
        if book['returned']:
            if book['return_date']:
                print(f"  Return Date : {book['return_date'].strftime('%Y-%m-%d')}")
            # ✅ Show fine paid status
            if book.get("fine_paid") is True:
                print("Fine Paid : Yes")
            elif book.get("fine_paid") is False:
                print("Fine Paid : No")
        # Always show fine
        print(f"  Fine (RM)   : {book['fine']:.2f}")


def search_book_by_title(books):
    """
    Searches for a book in the books list by its title (case-insensitive).
    The title is entered by the user.
    :param books: (list) list of book dictionaries
    :return: list of matching books
    """
    # Ask user for input instead of passing as parameter
    title = input("Enter the book title to search: ").strip()

    results = []
    for book in books:
        if book["title"].lower() == title.lower():  # case-insensitive match
            results.append(book)

    if results:
        print(f"\n✅ Found {len(results)} result(s) for '{title}':")
        for b in results:
            # Format dates safely
            borrow_str = b["borrow_date"].strftime("%Y-%m-%d") if hasattr(b["borrow_date"], "strftime") else str(b["borrow_date"])
            due_str = b["due_date"].strftime("%Y-%m-%d") if hasattr(b["due_date"], "strftime") else str(b["due_date"])

            print(f"\n📖 Title     : {b['title']}")
            print(f"   Borrower  : {b['borrower']}")
            print(f"   Borrowed  : {borrow_str}")
            print(f"   Due Date  : {due_str}")
            print(f"   Returned  : {'Yes' if b['returned'] else 'No'}")

            if b["returned"]:
                # Return date
                if b["return_date"]:
                    return_str = b["return_date"].strftime("%Y-%m-%d") if hasattr(b["return_date"], "strftime") else str(b["return_date"])
                    print(f"   Return Date: {return_str}")
                # Fine paid status
                if b.get("fine_paid") is True:
                    print("   Fine Paid : Yes")
                elif b.get("fine_paid") is False:
                    print("   Fine Paid : No")
            # Always show fine
            print(f"   Fine (RM) : {b['fine']:.2f}")
    else:
        print(f"\n❌ No book found with title '{title}'")

    return results


def search_book_by_borrower_name(books):
    """
    Procedure that searches for books by borrower name (case-insensitive).
    The borrower name is entered by the user.
    This function prints the search results directly, including borrower, title,
    borrow date, due date, returned status, return date, fine paid, and fine.
    
    :param books: (list) list of book dictionaries
    :return: None (results are displayed, not returned)
    """
    # Ask user for input instead of passing as parameter
    borrower = input("Enter the borrower name to search: ").strip()

    results = []
    for book in books:
        if book["borrower"].lower() == borrower.lower():  # case-insensitive match
            results.append(book)

    if results:
        print(f"\n✅ Found {len(results)} result(s) for '{borrower}':")
        for b in results:
            # Format dates safely
            borrow_str = b["borrow_date"].strftime("%Y-%m-%d") if hasattr(b["borrow_date"], "strftime") else str(b["borrow_date"])
            due_str = b["due_date"].strftime("%Y-%m-%d") if hasattr(b["due_date"], "strftime") else str(b["due_date"])

            print(f"\n📖 Title     : {b['title']}")
            print(f"   Borrower  : {b['borrower']}")
            print(f"   Borrowed  : {borrow_str}")
            print(f"   Due Date  : {due_str}")
            print(f"   Returned  : {'Yes' if b['returned'] else 'No'}")

            if b["returned"]:
                # Return date
                if b["return_date"]:
                    return_str = b["return_date"].strftime("%Y-%m-%d") if hasattr(b["return_date"], "strftime") else str(b["return_date"])
                    print(f"   Return Date: {return_str}")
                # Fine paid status
                if b.get("fine_paid") is True:
                    print("   Fine Paid : Yes")
                elif b.get("fine_paid") is False:
                    print("   Fine Paid : No")
            # Always show fine
            print(f"   Fine (RM) : {b['fine']:.2f}")
    else:
        print(f"\n❌ No book found with borrower name '{borrower}'")


  
def search_book_by_borrower_name_result(books):
    """
    Function that searches for books by borrower name (case-insensitive).
    The borrower name is entered by the user.
    Unlike the previous version, this function does not print anything.
    Instead, it returns a list of matching books so the caller can process or display them.
    
    :param books: (list) list of book dictionaries
    :return: list of matching book dictionaries (can be empty if no matches found)
    """
    # Ask user for input instead of passing as parameter
    borrower = input("Enter the borrower name to search: ").strip()

    results = []
    for book in books:
        if book["borrower"].lower() == borrower.lower():  # case-insensitive match
            results.append(book)
    return results


def display_total_fine_of_borrower(books):
    """
    Procedure that displays the total fine owed by a borrower.
    It searches for books borrowed by a given borrower, calculates
    the total overdue fine, and prints the result.

    :param books: (list) list of book dictionaries
    :return: None (prints the result instead of returning it)
    """
    # Search for all books borrowed by a user (case-insensitive)
    borrower_books = search_book_by_borrower_name_result(books)
    # If borrower has borrowed books
    if borrower_books:
        # Extract the borrower's name from the first book
        # (all books in the list belong to the same borrower)
        borrower = borrower_books[0]["borrower"]
        # Calculate total fine across all books for this borrower
        total_borrower_fine = calculate_total_borrower_fine(borrower_books)
        print(f"\n💰 Total fine of borrower '{borrower}': RM{total_borrower_fine:.2f}")
    else:
        print("\n❌ Borrower not found.")

    
def menu():
    """
    Procedure that displays the main Library Management System menu.
    It repeatedly asks the user to choose an option until they decide to exit.
    Each option calls the appropriate function to perform the action.
    """
    while True:
        # Display the main menu options
        print("\n===== Library Management Menu =====")
        print("1. Add a new book")
        print("2. Search for a book(s) by title")
        print("3. Search for a book(s) by borrower name")
        print("4. Display all books")
        print("5. Total fine of Borrower")
        print("6. Exit")
        
        # Get user input and remove extra spaces
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_books()
        elif choice == "2":
            search_book_by_title(books)
        elif choice == "3":
            search_book_by_borrower_name(books)
        elif choice == "4":
            display_all_books(books)
        elif choice == "5":
            display_total_fine_of_borrower(books)
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    menu()