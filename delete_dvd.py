import sqlite3
import utils
import modify_dvds
import dvd


class Multiline:

    delete_record = """===============================
DELETE A DVD RECORD:
===============================

Enter the title of the DVD to delete: """

    record_to_delete = """===============================
DVD TO DELETE:
==============================="""

    delete_confirmation = """        Are you sure you want to delete? Enter a choice and press enter
        (Y/y = yes, Anything else = No) """


def delete_record():
    """Deleting functionality for the program.
    """
    conn, c = utils.connect_to_db(utils.Config.DB_NAME)
    title = input(Multiline.delete_record),
    movie = c.execute(utils.SQLQuery.query_by_title, title).fetchone()
    print(Multiline.record_to_delete)
    if movie:
        utils.print_record(movie)
        print(utils.GenData.line_sep)
        conf_deletion = input(Multiline.delete_confirmation)
        if conf_deletion == 'Y' or conf_deletion == 'y':
            try:
                c.execute(utils.SQLQuery.delete_record, title)
            except sqlite3.DatabaseError:
                print(utils.GenData.db_error_msg)
                input(utils.GenData.enter_continue)
            else:
                conn.commit()
            finally:
                c.close()
                conn.close()
            print("Item deleted.")
            input(utils.GenData.enter_continue)

        else:
            print("Item NOT deleted.")
            input(utils.GenData.enter_continue)
    else:
        print("Record not found.")
        input(utils.GenData.enter_continue)
