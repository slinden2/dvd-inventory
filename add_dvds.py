import sqlite3
import utils


class Multiline:

    add_dvd = """===============================
ADD A DVD TO THE DATABASE:
==============================="""


def add_dvd():
    """Uploads dvd info to the DB.
    """
    conn, c = utils.connect_to_db(utils.Config.DB_NAME)
    new_dvd = get_dvd_info()
    try:
        c.execute(utils.SQLQuery.insert_new_dvd, new_dvd)
    except sqlite3.DatabaseError:
        print(utils.GenData.db_error_msg)
        input(utils.GenData.enter_continue)
    else:
        conn.commit()
        print("Record added.")
        input(utils.GenData.enter_continue)
    finally:
        c.close()
        conn.close()


def get_dvd_info():
    """Takes input from user for creating new dvd in the DB.

    :returns: tuple
    """
    print(Multiline.add_dvd)
    title = input("Enter the DVD title: ")
    star = input("Enter the name of the movie's star: ")
    costar = input("Enter the name of the movie's costar: ")
    year = utils.get_year_input()
    genre = utils.get_genre_input()
    return title, star, costar, year, genre
