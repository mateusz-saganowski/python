import sqlite3
from sqlite3 import Error
from task import task

task_list = []


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


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
    task_list.append(new)
    choice = input("Chcesz dodać kolejne zadanie [T/N]? ")
    if choice == "N" or choice == "n":
        main_menu()
    elif choice == "T" or choice == "t":
        new_task()
    else:
        print("Błędny wybór")
        return_to_menu()


def complete_task():
    print("tu będą zadania zrobione pobrane z bazy danych")
    return_to_menu()


def incomplete_task():
    print("tu będą zadania do zrobienia pobrane z bazy danych")
    for index in task_list:
        print(index.name)
    return_to_menu()


if __name__ == "__main__":
    create_connection(r"C:\Users\mateusz.saganowski\PycharmProjects\pythonProject\pythonsqlite.db")
    while True:
        main_menu()