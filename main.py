print("1: Wyświetlenie listy zrobionych zadań")
print("2: Wyświetlenie listy zadań do wykonania")
print("3: Dodaj zadanie")
print("0: Wyjdź")
while True:
    odpowiedz = input('Wybierz menu ')
    if odpowiedz == "3":
        nowe_zadanie = input("Napisz jakie zadanie chcesz dodać: ")
    if odpowiedz == "2":
        print(nowe_zadanie)
    if odpowiedz == "0":
        break
    if odpowiedz == "1":
        print("nic nie wykonałeś jeszcze łajzo!")