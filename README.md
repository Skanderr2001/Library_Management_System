# 📚 Library Management System

A modular, menu-driven Library Management System built in Python to manage borrowed books, track due dates, and calculate overdue fines.

---

## 👤 Author

**Skander Radhouane**  
Master of Science in Data Science and Business Analytics  
Major in Data Engineering
  

---

## 📌 Project Overview

This project is a console-based Library Management System designed to simulate real-world borrowing operations.

The system allows librarians to:

- Register borrowed books
- Track due and return dates
- Automatically calculate overdue fines
- Search books by title
- Search books by borrower
- Display all records
- Calculate total fines per borrower

The project emphasizes modular design, clean structure, and reliable input validation.

---

## 🏗️ System Architecture

### Data Structure

Each book is represented as a dictionary:

```python
{
    "title": str,
    "borrower": str,
    "borrow_date": datetime,
    "due_date": datetime,
    "returned": bool,
    "return_date": datetime or None,
    "fine": float,
    "fine_paid": bool or None
}
```

All book records are stored in a global list:

```python
books = []
```

---

## ⚙️ Core Functionalities

### Book Management
- Add new borrowed books
- Validate user input
- Prevent invalid dates
- Store structured records

### Fine Management
- RM 0.80 per overdue day
- Automatic calculation for:
  - Late returns
  - Books not yet returned
- Fine reset if marked as paid

### Search and Reporting
- Search by title (case-insensitive)
- Search by borrower (case-insensitive)
- Display complete borrowing records
- Calculate total fines per borrower

---

## 🧩 Function Documentation

### `calculate_overdue_fine(book)`
Calculates the overdue fine for a single book.

- If fine is already paid → returns 0
- If returned late → calculates overdue days × RM 0.80
- If not returned and overdue → calculates current overdue
- Updates the book dictionary with the calculated fine

---

### `add_books()`
Handles the addition of new book records.

- Collects user input
- Validates title and borrower
- Validates date format (YYYY-MM-DD)
- Ensures due date is after borrow date
- Handles return status and fine payment
- Stores book in the global list
- Allows multiple book entries in one session

---

### `calculate_total_borrower_fine(books)`
Calculates the total fine for all books borrowed by one borrower.

- Iterates through borrower’s books
- Calls `calculate_overdue_fine()` for each book
- Returns total fine amount

---

### `display_all_books(books)`
Displays all stored book records.

- Shows borrowing details
- Shows return status
- Shows fine and fine payment status
- Handles empty system case

---

### `search_book_by_title(books)`
Searches for books by title.

- Case-insensitive exact match
- Displays full book details
- Returns matching results list

---

### `search_book_by_borrower_name(books)`
Searches books by borrower name.

- Case-insensitive match
- Displays all books borrowed by that person

---

### `search_book_by_borrower_name_result(books)`
Internal helper function.

- Returns list of books borrowed by a specific person
- Used for fine calculation function

---

### `display_total_fine_of_borrower(books)`
Displays total fine owed by a borrower.

- Retrieves borrower’s books
- Calculates total fine
- Prints final amount

---

### `menu()`
Main system controller.

- Displays menu options
- Handles user selection
- Calls appropriate functions
- Runs continuously until exit

---

## 🛠️ Technologies Used

- Python 3.x
- `datetime` module
- Lists and Dictionaries
- Control Structures
- Exception Handling

---

## 🚀 How to Run

```bash
python filename.py
```

Replace `filename.py` with your script name.

---

## 📈 Future Improvements

- Database integration
- Graphical User Interface
- Unique book identifiers
- Persistent storage
- Authentication system
- Export reports to file

---

## 📊 Key Strengths

- Modular design
- Strong validation
- Real-time fine calculation
- Clean separation of responsibilities
- Easily extendable architecture

---

## 🎓 Academic Purpose

This project demonstrates:

- Python programming fundamentals
- Data structure usage
- Structured program design
- Logical problem solving
- Software modularity principles
