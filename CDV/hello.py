

'''math'''
print('LICZBA PI')

import math

pi = math.pi
print(pi)

'''pierwiastek'''
print('PIERWIASTEK')

pierwiastek = math.sqrt(9)

'''random'''
print()

import random

losuj = random.random()
print(losuj)

losujZlisty = random.choice([1,2,3,4])
print(losujZlisty)

'''
ZAD DOM
user podaje z klawiatury 2 wartości, maksymalną i minimalną z przedziału z którego bedzie 
wylosowane 5 liczb caukowitych. Liczby wylosowane wyświetl w formacie 
liczba 1:
liczba 2:
liczba 3:
'''

'''Instrukcje warunkowe'''
print('INSTRUKCJE WARUNKOWE')

x = 5
if x == 5:
    print('x jest równe 5')
else:
    print('x nie jest równe 5')

'''INNE'''
print('INNE')

y = True

if y:
    print('prawda')
else:
    print('nie prawda')

'''INNE 2'''
print('inne 2')

j = False
if bool(j):
    print(1)
else:
    print(0)







'''LISTY Z ROZSZERZENIEM PY'''
print('LISTY Z ROZSZERZENIEM PY')

programowanie = ['Python', 'PHP', 'C#', 'JS', 'Java']

print(programowanie)
print(type(programowanie))

pierwszy = programowanie[0]
print(pierwszy)

trzypierwsze = programowanie[0:3]
print(trzypierwsze)

ostatni = programowanie[-1]
print(ostatni)


programowanie.append('R')
programowanie.append('Python')
print(programowanie)




'''ZLICZANIE ELEMENTÓW W LIŚCIE'''
print('ZLICZANIE ELEMENTÓW PYTHON W LIŚCIE')

ile = programowanie.count('Python')
print(ile)


iloscElem = len(programowanie)
print(iloscElem)

innejezyki = ['C', 'C++']
programowanie.extend(innejezyki)
print(programowanie)


nowa = programowanie
print('Lista nowa: ', end='')
print(nowa)
nowa.clear()
print('Lista nowa: ', end='')
print(nowa)
print('Lista programowanie: ', end='')


'''LISTY'''
imiona = ['Julia', 'Anna', 'Krystyna']
print(type(imiona))
imiona.append('Janusz')
ilosc = len(imiona)
print(f'Ilość imion: (ilosc) ')


nazwiska = ('Kowalski', 'Nowak')
print(type(nazwiska))
print(nazwiska)


'''SŁOWNIK'''

slownik = {'klucz':'wartosc1','klucz2':'wartosc2'}

'''
Utwórz słownik o nazwie pracownik zawierający klucze: 
imie, nazwisko, imionaDzieci, imionaRodiców 


'''

pracownik = {
    'imie':'Anna',
    'nazwisko':'Nowak',
    'miasto':'Poznan',
    'wiek':'23',
    'imionaDzieci':['Anna','Tomasz'],
    'imionaRodzicow':['Julia','Jan'],
}

print(pracownik)
print(pracownik['imionaDzieci'])
print(pracownik ['imionaDzieci'])

'''    '''




pracownik1 = {
    'imie':'Anna',
    'nazwisko':'Nowak',
    'miasto':'Poznan',
    'wiek':'23',
    'imionaDzieci':['Anna','Tomasz'],
    'imionaRodzicow':['Julia','Jan'],
}

print()
print(pracownik1)

klucz='wiek'
if klucz in pracownik:
    del pracownik1[klucz]
    print(f'klucz {klucz} został usunięty')
else:
    print(f'klucz {klucz} nie został usunięty')

    print(pracownik1)
    print(pracownik1.keys())
    print(pracownik1.values())
    print(list(pracownik1.values()))
    print(pracownik1.items())

    for value in pracownik1.values():
        print(value, end='')


''' '''

def witaj():
    print('Witaj Janusz!')

    witaj()

    def wyswietlWiek(wiek):
        print(f'Twój wiek to{wiek}')

        wyswietlWiek(23)

        def iloczyn(a, b):
            return a * b

        print(iloczyn(3, 4))

        def iloraz(a, b):
            return a / b

        iloraz1 = iloraz(3, 4)
        print(iloraz1)
        print(type(iloraz1))

        print(iloraz(b=5, a=2))

        ''

























































