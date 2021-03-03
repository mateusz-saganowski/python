import sqlite3
from sqlite3 import Error
from task import task

task_list = []
database = r"C:\Users\mateusz.saganowski\PycharmProjects\pythonProject\pythonsqlite.db"


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,status)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def main_db_upload(upload):
    # create a database connection
    conn = create_connection(database)

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        status bool NOT NULL
                                    );"""
    # create tables
    if conn is not None:

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")
    with conn:
        # create tasks
        new_task = (upload.name, upload.status)
        create_task(conn, new_task)


def main_db_download(status):
    # create a database connection
    conn = create_connection(database)

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        status bool NOT NULL
                                    );"""
    # create tables
    if conn is not None:

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")
    with conn:
        # create tasks
        select_task_by_status(conn, status)


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_status(conn, status):
    """
    Query tasks by status
    :param conn: the Connection object
    :param status:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE status=?", (status,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main_menu():
    print("1: Wyświetlenie listy zrobionych zadań")
    print("2: Wyświetlenie listy zadań do wykonania")
    print("3: Dodaj zadanie")
    print("0: Wyjście")
    choice = input('Wybierz menu: ')
    if choice == "1":
        complete_task()
    elif choice == "2":
        incomplete_task()
    elif choice == "3":
        new_task()
    elif choice == "0":
        exit()
    else:
        print("Błędny wybór")


def return_to_menu():
    choice = input('Wyjście z programu [T/N]? ')
    if choice == "N" or choice == "n":
        main_menu()
    elif choice == "T" or choice == "t":
        exit()
    else:
        print("Błędny wybór")
        return_to_menu()


def new_task():
    print("Podaj nazwę nowego zadania: ")
    new = task(input(), False)
    main_db_upload(new)
    choice = input("Chcesz dodać kolejne zadanie [T/N]? ")
    if choice == "N" or choice == "n":
        main_menu()
    elif choice == "T" or choice == "t":
        new_task()
    else:
        print("Błędny wybór")
        return_to_menu()


def complete_task():
    print("Zrobione zadania pobrane z bazy danych")
    main_db_download(True)
    return_to_menu()


def incomplete_task():
    print("Pobrane zadania do zrobienia z bazy danych")
    main_db_download(False)
    return_to_menu()


if __name__ == "__main__":
    while True:
        main_menu()