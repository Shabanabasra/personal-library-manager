# personal-library-manager
Objective Create a command-line Personal Library Manager that allows users to manage their book collection. The program should let users add, remove, and search for books. Each book will be stored as a dictionary with details like title, author, publication year, genre, and read status. The program should also include a menu system, basic statistics, and optional file handling for saving and loading the library.

Requirements Core Features Book Details: Each book should have the following attributes:

Title (string) Author (string) Publication Year (integer) Genre (string) Read Status (boolean: True if read, False if unread) Menu System: Implement a menu with the following options:

Add a book Remove a book Search for a book Display all books Display statistics (total books, percentage read) Exit Add a Book: Prompt the user to enter the book's details and add it to the library.

Remove a Book: Prompt the user to enter the title of the book to remove it from the library.

Search for a Book: Allow the user to search for a book by title or author. Display all matching books.

Display All Books: Show all books in the library in a formatted way.

Display Statistics:

Total number of books in the library. Percentage of books that have been read. Exit: Exit the program.

Optional Challenge (File Handling) Save Library to a File: Save the library data to a file (e.g., library.txt) when the program exits. Load Library from a File: Load the library data from the file when the program starts. Sample Output Menu Welcome to your Personal Library Manager!

Add a book
Remove a book
Search for a book
Display all books
Display statistics
Exit
Enter your choice:
Add a Book Enter the book title: The Great Gatsby
Enter the author: F. Scott Fitzgerald
Enter the publication year: 1925
Enter the genre: Fiction
Have you read this book? (yes/no): yes
Book added successfully!

Remove a Book Enter the title of the book to remove: The Great Gatsby
Book removed successfully!

Search for a Book Search by:

Title
Author
Enter your choice: 1
Enter the title: The Great Gatsby
Matching Books:
The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read
Display All Books Your Library:

The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read
1984 by George Orwell (1949) - Dystopian - Unread
Display Statistics Total books: 2
Percentage read: 50.0%

Exit Library saved to file. Goodbye!
