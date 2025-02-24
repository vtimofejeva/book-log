# Columns needed:
#  - month 
#  - year
#  - book's title
#  - book's author
#  - genre
#  - rating: excellent / okay / garbage

months_choice = {
    "1": "January",
    "2": "February", 
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October", 
    "11": "November", 
    "12": "December"
}
genre_choice = ["Historical", "Fiction", "Fantasy", "Sci-Fi", "Romance"]
rating_choice = {
    "1": "Excellent",
    "2": "Okay",
    "3": "Garbage"
}

def year_entry():
    try:
        y_entry = int(input("YEAR when you finished reading the book:\n"))
        if y_entry <=1900 or y_entry >=2100:
            print("Year must be valid: between 1900 and 2100. Try again: \n")
            y_entry = int(input())
        return y_entry
    except:
        print("A valid date/integer must be provided.\n")
        return year_entry()

def month_entry():
    m_entry = input("MONTH when you finished reading the book:\n").title()
    if m_entry in months_choice.values():
        return m_entry
    elif m_entry in months_choice.keys():
        m_entry = months_choice[m_entry]
        return m_entry
    else:
        print("Please, provide the month's name or number: \n")
        return month_entry()

def book_title():
    b_title = input("Book's TITLE: \n").title()
    if len(b_title) > 40:
        print("The title is too long, please, try again: \n")
        return book_title()
    elif len(b_title) <= 0:
        print("The title cannot be an empty string, please, try again: \n")
        return book_title()
    else:
        return b_title

def book_author():
    b_author = input("Book's AUTHOR: \n").title()
    if len(b_author) > 40:
        print("The name is too long, please, try again: \n")
        return book_author()
    elif len(b_author) <= 0:
        print("The name cannot be an empty string, please, try again: \n")
        return book_author()
    else:
        return b_author
    
def book_genre():
    b_genre = input("Book's GENRE? \n").title()
    if b_genre in genre_choice:
        return b_genre
    else:
        print("No such genre in the list.\n")
        view_genres = input("Would you like to see the genre list? - yes or no? \n")
        if view_genres == "yes":
            print(genre_choice)
            return book_genre()
        else:
            return book_genre()
        
def book_rating():
    b_rating = input("RATE the book::\n1.Excellent\n2.Okay\n3.Garbage\n").title()
    if b_rating in rating_choice.values():
        return b_rating
    elif b_rating in rating_choice.keys():
        b_rating = rating_choice[b_rating]
        return b_rating
    else:
        print("Please, select one of the 3 options:\n1.Excellent\n2.Okay\n3.Garbage\n")
        return book_rating()
