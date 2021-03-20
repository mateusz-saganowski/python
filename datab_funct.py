import sqlite3


def create_connection(db_file):
    """
        create a database connection to the SQLite database
        :param db_file:  name and location for database
        :return: Connection to the SQLite database
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


def create_task_table(conn):
    """
        Create a tasks table
        :param conn:  Connection to the SQLite database
        :return:
    """
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                                id integer PRIMARY KEY,
                                                name text NOT NULL,
                                                status bool NOT NULL
                                            );"""
    # create tables
    if conn is not None:
        # create tasks table
        try:
            c = conn.cursor()
            c.execute(sql_create_tasks_table)
        except sqlite3.Error as e:
            print(e)
    else:
        print("Error! cannot create the database connection.")


def prepare_db(conn):
    """
        Prepare database with table creation or use existing table
        :param conn:  Connection to the SQLite database
        :return:
    """
    create_task_table(conn)


def create_task(conn, task_name):
    """
        Create a new task
        :param conn:  Connection to the SQLite database
        :param task_name: Class for created task: name and status for the table in database
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
        :param conn:  Connection to the SQLite database
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
       :param conn:  Connection to the SQLite database
       :param status: selected status for query tasks
       :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE status=?", (status,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_id(conn, task_number):
    """
       Selected task by id from database
       :param conn:  Connection to the SQLite database
       :param task_number: id of the selected task
       :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE id=?", (task_number,))

    row = cur.fetchall()
    selected_task = row[0]

    return selected_task


def update_task_status(conn, update_task):
    """
       Update status of selected task in database
       :param conn:  Connection to the SQLite database
       :param update_task: id of the updated task
       :return:
    """
    sql = ''' UPDATE tasks
                 SET status = ? 
                 WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, update_task)
    conn.commit()


def update_task_name(conn, update_task):
    """
       Update name of selected task in database
       :param conn:  Connection to the SQLite database
       :param update_task: id of the updated task
       :return:
    """
    sql = ''' UPDATE tasks
                 SET name = ? 
                 WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, update_task)
    conn.commit()


def delete_task(conn, update_task):
    """
        Delete a task by task id in database
        :param conn:  Connection to the SQLite database
        :param update_task: id of the deleted task
        :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (update_task,))
    conn.commit()