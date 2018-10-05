import sqlite3


class Config:

    DB_NAME = "dvd.db"


class GenData:

    enter_continue = "Press <Enter> to continue."
    line_sep = "==============================="
    genres = ["Drama", "Horror", "Comedy", "Romance"]
    db_error_msg = "There was a problem accessing the record in the database!"
    columns = ["ID", "Title", "Star", "Costar", "Year", "Genre"]


class SQLQuery:

    insert_new_dvd = """INSERT INTO dvd (
                        dvd_title,
                        dvd_star_name,
                        dvd_costar_name,
                        dvd_year,
                        dvd_genre)
                        VALUES (?, ?, ?, ?, ?)"""
    query_by = "SELECT * FROM dvd WHERE ? = ?"
    query_by_title = "SELECT * FROM dvd WHERE dvd_title = ?"
    query_by_star = "SELECT * FROM dvd WHERE dvd_star_name = ?"
    query_by_costar = "SELECT * FROM dvd WHERE dvd_costar_name = ?"
    query_by_year = "SELECT * FROM dvd WHERE dvd_year = ?"
    query_by_genre = "SELECT * FROM dvd WHERE dvd_genre = ?"
    query_all_rows = "SELECT * FROM dvd"
    update_title = "UPDATE dvd SET dvd_title = ? WHERE dvd_title = ?"
    update_star = "UPDATE dvd SET dvd_star_name = ? WHERE dvd_title = ?"
    update_costar = "UPDATE dvd SET dvd_costar_name = ? WHERE dvd_title = ?"
    update_year = "UPDATE dvd SET dvd_year = ? WHERE dvd_title = ?"
    update_genre = "UPDATE dvd SET dvd_genre = ? WHERE dvd_title = ?"
    delete_record = "DELETE FROM dvd WHERE dvd_title = ?"


class Multiline:

    genre_input1 = """Enter the genre to apply to this DVD:
1 - Drama
2 - Horror
3 - Comedy
4 - Romance
Type the number for the genre
you want to apply and press <Enter>: """
    genre_input2 = """Enter the genre:
\t - 1 for drama, 2 for horror, 3 for comedy, 4 for romance: """


def get_user_input(n):
    """Takes input from the user allowing only specific integers.

    :param n: Number of valid inputs between 1 - n
    """
    user_input = ""
    valid_inputs = [x for x in range(1, n)]
    invalid_input = "Invalid input"
    while not user_input:
        try:
            user_input = int(input("Select a number: "))
        except:
            print(invalid_input)
        else:
            if user_input not in valid_inputs:
                user_input = ""
                print(invalid_input)
    return user_input


def get_year_input():
    """Takes a year input from the user.
    Accepts integers between 1900 - 2100.
    :returns: year (int)
    """
    year = ""
    while not year:
        try:
            year = int(input("Enter the year the movie was released: "))
        except ValueError:
            print("Invalid input")
        else:
            min_y, max_y = 1900, 2100
            if not min_y <= year <= max_y:
                year = ""
                print(f"Your input must be between {min_y} and {max_y}")
    return year


def get_genre_input(modify=False):
    """Takes genre input from the user. Must be an integer
    between 1 - 4.
    :param modify: This is used to change the text prompted
                    to the user in different use cases.
    :returns: genre (str)
    """
    if modify:
        print(Multiline.genre_input2)
    else:
        print(Multiline.genre_input1)
    genre = get_user_input(5)
    if genre == 1:
        genre = GenData.genres[0]
    elif genre == 2:
        genre = GenData.genres[1]
    elif genre == 3:
        genre = GenData.genres[2]
    elif genre == 4:
        genre = GenData.genres[3]
    return genre


def connect_to_db(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor


def print_record(movie):
    """Print out records neatly enumerated.
    :param movie: a dvd record from the db.
    """
    columns = GenData.columns
    for n, (column, data) in enumerate(zip(columns[1:], movie[1:]), start=1):
        print(f"{n} - {column:<10} {data}")
