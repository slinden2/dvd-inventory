import os
import sqlite3
import utils
import add_dvds
import lookup_dvds
import modify_dvds
import delete_dvd
import csvexport_dvd


class Multiline:

    main_menu = """================================
    DVD DATABASE
    ================================
    1 - Add a DVD to the database
    2 - Search inventory
    3 - Modify DVD record
    4 - Delete DVD record
    5 - Export listing to CSV
    6 - Exit
    ================================

Enter a choice and press enter:
"""


def menu():
    """Main menu of the program.
    """
    os.system('cls')
    print(Multiline.main_menu)

    user_input = utils.get_user_input(7)

    if user_input == 1:
        add_dvds.add_dvd()
        menu()

    elif user_input == 2:
        lookup_dvds.lookup_dvd()
        menu()

    elif user_input == 3:
        modify_dvds.modify_record()
        menu()

    elif user_input == 4:
        delete_dvd.delete_record()
        menu()

    elif user_input == 5:
        csvexport_dvd.generate_csv()
        menu()

    else:
        exit()


if __name__ == "__main__":

    menu()
