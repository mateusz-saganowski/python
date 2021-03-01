from zadania import zadania

lista = []
wyjscie = False


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
        global wyjscie
        wyjscie = True
    else:
        print("Błędny wybór")


def powrot_do_menu():
    odpowiedz = input('Wyjście z programu [T/N]? ')
    if odpowiedz == "N" or odpowiedz == "n":
        menu_glowne()
    elif odpowiedz == "T" or odpowiedz == "t":
        global wyjscie
        wyjscie = True
    else:
        print("Błędny wybór")
        powrot_do_menu()


def dodanie_zadania():
    print("Podaj nazwę nowego zadania: ")
    nowe = zadania(input(), False)
    lista.append(nowe)
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
    for test in lista:
        print(test.tytul)
    powrot_do_menu()


if __name__ == "__main__":
    while not wyjscie:
        menu_glowne()