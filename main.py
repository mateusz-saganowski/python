import sqlite3
from datab_funct import *
from task import Task


database = "pythonsqlite.db"


def main_menu():
    print("1: Wyświetlenie listy zrobionych zadań")
    print("2: Wyświetlenie listy zadań do wykonania")
    print("3: Dodaj zadanie")
    print("4: Edycja zadania")
    print("0: Wyjście")
    choice = input('Wybierz menu: ')
    if choice == "1":
        complete_task()
    elif choice == "2":
        incomplete_task()
    elif choice == "3":
        new_task()
    elif choice == "4":
        task_edition()
    elif choice == "0":
        exit()
    else:
        print("Błędny wybór")


def return_to_menu():
    choice = input('Wyjście z programu [t/N]? ')
    if choice.lower() == "n" or len(choice) == 0:
        main_menu()
    elif choice.lower() == "t":
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


def task_edition():
    task_number = input("Podaj numer ID zadania do edycji: ")
    if task_number.isdecimal() is False:
        print("Błędny wpis numeru zadania!")
        task_edition()
    elif task_number.isdecimal() is True:
        task_number = int(task_number)
        with conn:
            sel_task = select_task_by_id(conn, task_number)
            if sel_task is not None:
                choice = input("Edycja Statusu, nazwy czy usunięcie zadania [S/n/u]? ")
                if choice.lower() == "s" or len(choice) == 0:
                    sel_task_status = bool(sel_task[2])
                    if sel_task_status is False:
                        choice = input("Potwierdzasz zmianę statusu zadania na TRUE (T)? ")
                        if choice.lower() == "t" or len(choice) == 0:
                            update_task_status(conn, (True, task_number))
                        else:
                            main_menu()
                    elif sel_task_status is True:
                        choice = input("Potwierdzasz zmianę statusu zadania na False (T)? ")
                        if choice.lower() == "t" or len(choice) == 0:
                            update_task_status(conn, (False, task_number))
                        else:
                            main_menu()
                elif choice.lower() == "n":
                    print(sel_task[1])
                    update_name = input("Podaj poprawną nazwę edytowanego zadania: ")
                    update_task_name(conn, (update_name, task_number))
                    print("Nazwę zadania pomyślnie zmieniono w bazie danych")
                elif choice.lower() == "u":
                    delete_task(conn, task_number)
                    print("Zadanie pomyślnie usunięto z bazy danych")
                else:
                    print("Błędny wybór")
                    return_to_menu()
            else:
                print("Brak wybranego numeru zadania w tabeli bazy danych")
                select_all_tasks(conn)
                task_edition()


def complete_task():
    with conn:
        print("Zrobione zadania pobrane z bazy danych")
        select_task_by_status(conn, True)
    return_to_menu()


def incomplete_task():
    with conn:
        print("Pobrane zadania do zrobienia z bazy danych")
        select_task_by_status(conn, False)
    return_to_menu()


if __name__ == "__main__":
    conn = create_connection(database)
    prepare_db(conn)
    while True:
        main_menu()