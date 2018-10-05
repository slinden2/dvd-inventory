import sqlite3
import csv
import utils


class Multiline:

    export_database = """EXPORT DATABASE TO CSV:
===============================
Enter base filename (will be given a .csv extension): """


def generate_csv():
    """Exports a .csv file that corresponds to the columns
    in the DB.
    """
    conn, c = utils.connect_to_db(utils.Config.DB_NAME)
    fn = input(Multiline.export_database) + '.csv'
    db_rows = []
    try:
        db_rows = c.execute(utils.SQLQuery.query_all_rows).fetchall()
    except sqlite3.DatabaseError:
        print(utils.GenData.db_error_msg)
    else:
        conn.commit()
    finally:
        c.close()
        conn.close()
    if db_rows:
        with open(fn, 'w', newline='') as csv_f:
            fields = utils.GenData.columns
            writer = csv.DictWriter(csv_f, fieldnames=fields)
            writer.writeheader()
            for item in db_rows:
                writer.writerow({'ID': item[0], 'Title': item[1],
                                 'Star': item[2], 'Costar': item[3],
                                 'Year': item[4], 'Genre': item[5]})
        print(f"{fn} successfully written.")
        input(utils.GenData.enter_continue)
