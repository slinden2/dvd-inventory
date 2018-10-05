import utils


class Multiline:

    menu = """===============================
    DVD LOOKUP:
    ===============================
    Enter the criteria to look up by:
    1 - Movie title
    2 - Star
    3 - Costar
    4 - Year released
    5 - Genre
    6 - Main menu

Type a number and press enter:
"""
    search_results = """===============================
DVD SEARCH RESULTS:"""

    search_by_genre = """Enter the genre to search for:
1 - Drama
2 - Horror
3 - Comedy
4 - Romance
"""


def lookup_dvd():
    """Menu structure for searching DVDs from the DB.
    """
    print(Multiline.menu)

    user_input = utils.get_user_input(7)

    if user_input == 1:
        search_field = "title"
        query = utils.SQLQuery.query_by_title
        print_query_results(search_field, query)

    elif user_input == 2:
        search_field = "star"
        query = utils.SQLQuery.query_by_star
        print_query_results(search_field, query)

    elif user_input == 3:
        search_field = "costar"
        query = utils.SQLQuery.query_by_costar
        print_query_results(search_field, query)

    elif user_input == 4:
        search_field = "release year"
        query = utils.SQLQuery.query_by_year
        print_query_results(search_field, query)

    elif user_input == 5:
        is_genre = True
        search_field = "genre"
        query = utils.SQLQuery.query_by_genre
        print_query_results(search_field, query, is_genre)


def print_query_results(search_field, query, is_genre=False):
    """Gets dvds from the DB and prints out the results.

    :param search_field: Used for showing what is going to be
                        searched for the user.
    :param query: SQL query to be executed.
    :param is_genre: if the user searches by genre the search must
                    done with some additional functionality.
    """
    conn, c = utils.connect_to_db(utils.Config.DB_NAME)
    if is_genre:
        genre = utils.GenData.genres
        print(Multiline.search_by_genre)
        user_input = utils.get_user_input(len(genre + 1))
        search_str = genre[user_input-1],
    else:
        # Trailing comma because the variable must be a tuple
        search_str = input(f"Enter the DVD {search_field} to search for: "),
    movies = c.execute(query, search_str).fetchall()
    print(Multiline.search_results)
    print(utils.GenData.line_sep)
    if movies:
        for movie in movies:
            utils.print_record(movie)
            print(utils.GenData.line_sep)
    else:
        print(f"No records found with that {search_field}.")
        print(utils.GenData.line_sep)
    c.close()
    conn.close()
    input(utils.GenData.enter_continue)
