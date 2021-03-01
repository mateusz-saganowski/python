from zadania import zadania

lista = []


def menu_glowne():
    print("1: Wyświetlenie listy zrobionych zadań")
    print("2: Wyświetlenie listy zadań do wykonania")
    print("3: Dodaj zadanie")
    print("0: Wyjście")
    odpowiedz = input('Wybierz menu: ')
    if odpowiedz == "1":
        zrobione_zadania()
    elif odpowiedz == "2":
        zadania_do_zrobienia()
    elif odpowiedz == "3":
        dodanie_zadania()
    elif odpowiedz == "0":
        exit()
    else:
        print("Błędny wybór")


def powrot_do_menu():
    odpowiedz = input('Wyjście z programu [T/N]? ')
    if odpowiedz == "N" or odpowiedz == "n":
        menu_glowne()
    elif odpowiedz == "T" or odpowiedz == "t":
        exit()
    else:
        print("Błędny wybór")
        powrot_do_menu()


def dodanie_zadania():
    print("Podaj nazwę nowego zadania: ")
    nowe = zadania(input(), False)
    print(nowe.tytul, nowe.status)
    lista.append(nowe.tytul)
    odpowiedz = input("Chcesz dodać kolejne zadanie [T/N]? ")
    if odpowiedz == "N" or odpowiedz == "n":
        menu_glowne()
    elif odpowiedz == "T" or odpowiedz == "t":
        dodanie_zadania()
    else:
        print("Błędny wybór")
        powrot_do_menu()


def zrobione_zadania():
    print("tu będą zadania zrobione pobrane z bazy danych")
    powrot_do_menu()


def zadania_do_zrobienia():
    print("tu będą zadania do zrobienia pobrane z bazy danych")
    print(lista)
    powrot_do_menu()


if __name__ == "__main__":
    while True:
        menu_glowne()