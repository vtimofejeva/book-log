# for this project we use Finance_Tracker as a template, but we not gonna implement graphs (matplotlib)

# Purpose: track books that I am reading per month/year
# Columns needed:
#  - month and year
#  - book's title
#  - book's author
#  - genre
#  - rating: excellent / okay / garbage
# Files required: 
#  1. main loop of the program
#  2. extra: define input of the data entry for each column

import pandas as pd
import csv
from data_input import year_entry, month_entry, book_title, book_author, book_genre, book_rating

class CSV:
    global csv_file
    csv_file = "book_log.csv"
    columns = ["YEAR", "MONTH", "TITLE", "AUTHOR", "GENRE", "RATING"]
    
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(csv_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.columns)
            df.to_csv(csv_file, index=False)

    @classmethod
    def add_entry(cls, y_entry, m_entry, b_title, b_author, b_genre, b_rating):
        new_entry = {
            "YEAR": y_entry,
            "MONTH": m_entry,
            "TITLE": b_title,
            "AUTHOR": b_author,
            "GENRE": b_genre,
            "RATING": b_rating
        }
        with open(csv_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.columns)
            writer.writerow(new_entry)
        print("Entry added successfully!")

def adding_entries():
    CSV.initialize_csv()
    y_entry = year_entry() 
    m_entry = month_entry()
    b_title = book_title()
    b_author = book_author()
    b_genre = book_genre()
    b_rating = book_rating()
    CSV.add_entry(y_entry, m_entry, b_title, b_author, b_genre, b_rating)

def main():
    print("Welcome to the Book Log!\nChoose a menu option to start:")
    while True:
        print("\n1. View the logs")
        print("2. Add a new log")
        print("3. Exit\n")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            viewing = pd.read_csv(csv_file)
            print(viewing)
        elif choice == "2":
            adding_entries()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")

if __name__ == "__main__":
    main()    


#CSV.initialize_csv()
#CSV.add_entry("January", "2025", "Say Nothing", "Patrick Radden Kelly", "historical", "excellent")