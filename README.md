## Books Management Project
### Objective
In this project, our main goal is to create a project that combines control flow, functions, lists, and dictionaries.

### Problem
create a program that adds and displays information about a list of books. Each book is a dictionary that has the following keys: **title, author,** and the **year** of publication.

### Implementation

- Create an empty list `books` to store the book's dictionaries.
- Write a function `add_book` to add a book to the list. The function should take the title, author, and year as arguments and add the book to the list as a dictionary.
- Write a function `display` to print all the book's dictionaries in the list using a for loop.
- Create a `while` loop that asks the user to add a book or display the books. The loop should continue until the user chooses to exit.
- Inside the loop, display menu with the following options:
  * Add a book (1)
  * Display books (2)
  * Exit (3)
- Based on the user's choice, perform the following actions:
  * If the choice is 1, ask the user to enter the book data and call the `add_book` function.
  * If the choice is 2, call the `display` function to print all the books.
  * If the choice is 3, exit the loop.
  * If the user enters an invalid choice, print "Invalid choice. Please try again".

