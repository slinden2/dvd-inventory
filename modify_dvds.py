import sqlite3
import dvd
import utils
import lookup_dvds
import add_dvds


class Multiline:

    modify_record_title = """===============================
MODIFY A DVD RECORD:
===============================

Enter the title of the DVD to modify: """

    modify_record = """===============================
DVD TO MODIFY:
==============================="""

    modified_record = """===============================
MODIFIED RECORD:
==============================="""


def modify_record():
    """Modifies a dvd record in the DB.
    """
    conn, c = utils.connect_to_db(utils.Config.DB_NAME)
    title = input(Multiline.modify_record_title),  # tuple
    movie = c.execute(utils.SQLQuery.query_by_title, title).fetchone()
    print(Multiline.modify_record)
    if movie:
        utils.print_record(movie)
        print(utils.GenData.line_sep)
        user_input = utils.get_user_input(6)

        if user_input == 1:
            new_title = input("Enter the new DVD title name: "),
            update_column(conn, c, utils.SQLQuery.update_title,
                          new_title[0], title[0])
            mod_movie = get_modified_movie(
                c, utils.SQLQuery.query_by_title, new_title)
        elif user_input == 2:
            new_star = input("Enter the new DVD star name: ")
            update_column(conn, c, utils.SQLQuery.update_star,
                          new_star, title[0])
            mod_movie = get_modified_movie(
                c, utils.SQLQuery.query_by_title, title)
        elif user_input == 3:
            new_costar = input("Enter the new DVD costar name: ")
            update_column(conn, c, utils.SQLQuery.update_costar,
                          new_costar, title[0])
            mod_movie = get_modified_movie(
                c, utils.SQLQuery.query_by_title, title)
        elif user_input == 4:
            new_year = utils.get_year_input()
            c.execute(utils.SQLQuery.update_year, (new_year, title[0]))
            conn.commit()
            mod_movie = c.execute(utils.SQLQuery.query_by_title,
                                  title).fetchone()
        elif user_input == 5:
            new_genre = utils.get_genre_input(modify=True)
            c.execute(utils.SQLQuery.update_genre, (new_genre, title[0]))
            conn.commit()
            mod_movie = c.execute(utils.SQLQuery.query_by_title,
                                  title).fetchone()

        print(Multiline.modified_record)
        utils.print_record(mod_movie)
        c.close()
        conn.close()
        print(utils.GenData.line_sep)
        input(utils.GenData.enter_continue)
    else:
        print("Record not found.")
        input(utils.GenData.enter_continue)


def update_column(conn, cursor, query, new_value, title):
    """Provides error handling for DB modifications.
    :param conn: DB connection
    :param cursor: DB cursor
    :param query: SQL query
    :param new_value: A new value to be inserted into the DB.
    :param title: The dvd_title of the record to be modified.
    """
    try:
        cursor.execute(query, (new_value, title))
    except sqlite3.DatabaseError:
        print(utils.GenData.db_error_msg)
    else:
        conn.commit()


def get_modified_movie(cursor, query, value):
    """Gets the modified record from the DB.
    :param cursor: DB cursor
    :param query: SQL query
    :param value: The filter value for the SQL query
    :returns: modified record (tuple)
    """
    mod_movie = ""
    try:
        mod_movie = cursor.execute(query, new_value).fetchone()
    except sqlite3.DatabaseError:
        print(print(utils.GenData.db_error_msg))
    return mod_movie
