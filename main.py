print("Wyświetlenie listy zrobionych zadań: 1")
print("Wyświetlenie listy zadań do wykonania: 2")
print("Dodaj zadanie: 3")
while True:
    odpowiedz = input('Wybierz menu ')
    if odpowiedz == "3":
        nowe_zadanie = input("Napisz jakie zadanie chcesz dodać: ")
        print(nowe_zadanie)
        break