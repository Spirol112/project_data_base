import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


def menu():
    print("-------------------MENU------------------")
    print("-----1.Odczytaj baze danych z pliku------")
    print("--------------2.Dodaj wpis---------------")
    print("---------------3.Usuń wpis---------------")
    print("---------4.posortuj baze danych----------")
    print("-----------5.Pokaż baze danych-----------")
    print("-6.Pokaż wykres wzrostu od rozmiaru buta-")
    print("------7.Zapisz baze danych do pliku------")
    print("---------------8.Wyjście-----------------")


def menu2():
    print("--------------Sortuj według:------------")
    print("----------------1.Imienia---------------")
    print("----------------2.Wieku-----------------")
    print("----------------3.Wzrostu---------------")
    print("----------------4.Cofnij----------------")


def insert():
    name = str(input("Podaj imie: "))
    age = int(input("Podaj wiek: "))
    shoe_size = int(input("Podaj rozmiar buta: "))
    height = int(input("Podaj wzrost: "))
    favourite_book = str(input("Podaj tytuł ulubionej książki: "))
    favourite_film = str(input("Podaj tytuł ulubionego filmu: "))
    return [name, age, shoe_size, height, favourite_book, favourite_film]


def add(data1):
    tab = insert()
    data1 = data1.append(
        {'Name': tab[0], 'Age': tab[1], 'Shoe_size': tab[2], 'Height': tab[3], 'Favourite_book': tab[4],
         'Favourite_film': tab[5]}, ignore_index=True)
    return data1


def sort(data2):
    while 1:
        menu2()
        choice2 = int(input("Opcje: "))
        if choice2 == 1:
            data2 = data2.sort_values('Name')
            return data2
        elif choice2 == 2:
            data2 = data2.sort_values('Age')
            return data2
        elif choice2 == 3:
            data2 = data2.sort_values('Height')
            return data2
        elif choice2 == 4:
            break
        else:
            print("Nie Ma takiej opcji!!!")


def check():
    c = False
    while not c:
        try:
            variable = int(input())
            if variable < 0:
                print("Podana wartość nie może być ujemna")
            if variable >= 0:
                c = True
        except:
            print("Podana wartość nie może być ciągiem znaków")
    return variable


data = pd.DataFrame({
    'Name': ['#default'],
    'Age': [0],
    'Shoe_size': [0],
    'Height': [0],
    'Favourite_book': ['#default'],
    'Favourite_film': ['#default']
})

while 1:
    menu()
    choice = int(input("Opcja: "))
    if choice == 1:
        data = pd.read_csv('data.csv')

    elif choice == 2:
        data = add(data)

    elif choice == 3:
        number = int(input("Podaj numer komurki którą chcesz usunąć: "))
        data = data.drop(number)

    elif choice == 4:
        data = sort(data)

    elif choice == 5:
        print(data)

    elif choice == 6:
        data = data.sort_values('Height')
        data.plot(y='Height')
        data = data.sort_values('Shoe_size')
        data.plot(x='Shoe_size')
        plt.show()

    elif choice == 7:
        # zapisujemy DataFrame do pliku csv
        data.to_csv('data.csv', index=False)

    elif choice == 8:
        break
    else:
        print("Nie ma takiej opcji!!!")
