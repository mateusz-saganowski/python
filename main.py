import sqlite3
from task import Task

task_list = []
database = "pythonsqlite.db"


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
    except sqlite3.Error as e:
        print(e)

    return conn


def create_task_table(conn):
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                                id integer PRIMARY KEY,
                                                name text NOT NULL,
                                                status bool NOT NULL
                                            );"""
    # create tables
    if conn is not None:
        # create tasks table
        """ create a table from the create_table_sql statement
            :param conn: Connection object
            :param create_table_sql: a CREATE TABLE statement
            :return:
            """
        try:
            c = conn.cursor()
            c.execute(sql_create_tasks_table)
        except sqlite3.Error as e:
            print(e)
    else:
        print("Error! cannot create the database connection.")


def prepare_db():
    conn = create_connection(database)
    create_task_table(conn)


def create_task(conn, task_name):
    """
    Create a new task
    :param conn:
    :param task_name:
    :return:
    """

    sql = """ INSERT INTO tasks(name,status)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, task_name)
    conn.commit()
    return cur.lastrowid


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
    choice = input('Wyjście z programu [T/n]? ')
    if choice.lower() == "n":
        main_menu()
    elif choice.lower() == "t" or len(choice) == 0:
        exit()
    else:
        print("Błędny wybór")
        return_to_menu()


def new_task():
    print("Podaj nazwę nowego zadania: ")
    new = Task(input(), False)
    if len(new.name) == 0:
        print("Nie podano poprawnej nazwy zadania!")
        new_task()
    else:
        conn = create_connection(database)
        with conn:
            create_new_task = (new.name, new.status)
            create_task(conn, create_new_task)
        choice = input("Chcesz dodać kolejne zadanie [T/n]? ")
        if choice.lower() == "n":
            main_menu()
        elif choice.lower() == "t" or len(choice) == 0:
            new_task()
        else:
            print("Błędny wybór")
            return_to_menu()


def complete_task():
    conn = create_connection(database)
    with conn:
        print("Zrobione zadania pobrane z bazy danych")
        select_task_by_status(conn, True)
    return_to_menu()


def incomplete_task():
    conn = create_connection(database)
    with conn:
        print("Pobrane zadania do zrobienia z bazy danych")
        select_task_by_status(conn, False)
    return_to_menu()


if __name__ == "__main__":
    prepare_db()
    while True:
        main_menu()