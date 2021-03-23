import datab_funct
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
    while True:
        task_name = input("Podaj nazwę nowego zadania: ")
        if len(task_name) > 0:
            break
        print("Nie podano poprawnej nazwy zadania!")

    new = Task(task_name, False)
    with conn:
        create_new_task = (new.name, new.status)
        datab_funct.create_task(conn, create_new_task)
    choice = input("Chcesz dodać kolejne zadanie [T/n]? ")
    if choice.lower() == "n":
        main_menu()
    elif choice.lower() == "t" or len(choice) == 0:
        new_task()
    else:
        print("Błędny wybór")
        return_to_menu()


def task_edition():
    while True:
        task_id = input("Podaj numer ID zadania do edycji: ")
        if task_id.isdecimal():
            task_id = int(task_id)
            with conn:
                sel_task = datab_funct.select_task_by_id(conn, task_id)
                if sel_task is not None:
                    break
        print("Błędny wpis lub brak wybranego numeru zadania z tabeli bazy danych!")
        datab_funct.select_all_tasks(conn)
    with conn:
        choice = input("Edycja Statusu, nazwy czy usunięcie zadania [S/n/u]? ")
        if choice.lower() == "s" or len(choice) == 0:
            sel_task_status = bool(sel_task[2])
            choice = input(f"Potwierdzasz zmianę statusu zadania na {not sel_task_status} (T)? ")
            if choice.lower() == "t" or len(choice) == 0:
                datab_funct.update_task_status(conn, (not sel_task_status, task_id))
            else:
                main_menu()
        elif choice.lower() == "n":
            print(sel_task[1])
            update_name = input("Podaj poprawną nazwę edytowanego zadania: ")
            datab_funct.update_task_name(conn, (update_name, task_id))
            print("Nazwę zadania pomyślnie zmieniono w bazie danych")
        elif choice.lower() == "u":
            datab_funct.delete_task(conn, task_id)
            print("Zadanie pomyślnie usunięto z bazy danych")
        else:
            print("Błędny wybór")
            return_to_menu()


def complete_task():
    with conn:
        print("Zrobione zadania pobrane z bazy danych")
        datab_funct.select_task_by_status(conn, True)
    return_to_menu()


def incomplete_task():
    with conn:
        print("Pobrane zadania do zrobienia z bazy danych")
        datab_funct.select_task_by_status(conn, False)
    return_to_menu()


if __name__ == "__main__":
    conn = datab_funct.create_connection(database)
    datab_funct.prepare_db(conn)
    while True:
        main_menu()