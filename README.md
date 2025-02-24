# Book Log [Python]
A simple CLI-based book logging system that helps track books you read per month and year.

Features:
- Store book details such as title, author, genre, and rating.
- Track books read per month and year.
- View your logged books in a structured CSV file book_log.csv.
- Simple CLI interface for easy data entry.

Project Structure:
- main.py          - Main script to run the book logging system  
- data_input.py    - Handles user input (not included in this repo yet)  
- book_log.csv     - Stores book entries (auto-generated)
- README.md        - Project documentation  

Dependencies:
This project requires Pandas. Install it via: pip install pandas  

How to Use:
- Run main.py.
- Choose from the menu options:
   1: View logged books.
   2: Add a new book entry.
      Follow the prompts to enter book details.
   3: Exit the program.

Data Fields:
- YEAR - Year of reading - 2024
- MONTH	- Month of reading -	January
- TITLE	- Title - Dune
- AUTHOR - Author -	Frank Herbert
- GENRE	- Genre	- Sci-Fi
- RATING - Personal	Rating (Excellent / Okay / Garbage)	- Excellent
