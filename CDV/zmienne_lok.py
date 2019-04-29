# Zasięg zmiennych, zmienne lokalne i globalne


# Precyzja liczby (zaokrąglenie do 3 miejsc po przecinku liczby
# 5: 5.000
x = "{0:.3f}".format(5)
print(x)


def plnToChf(value):
    kursChf = 3.7913
    iloscChf = value / kursChf
    iloscChf = "{0:.4f}".format(iloscChf)
    print(iloscChf)


plnToChf(1000)

"""
 Utworz funkcję zwracającą ilość Euro, jaką klient może kupić za PLN
 
"""


def plnToEur(value):
    kursEur = 4.2927
    iloscEur = value / kursEur
    iloscEur = "{0:.0f}".format(iloscEur)
    print(iloscEur)


plnToEur(1000)

# Zmienna globalna
kursUSD = 3.50
print(f'ID USD: {id(kursUSD)}')


def plnToUSD(value):
    kursUSD = 4.00
    iloscUSD = value / kursUSD
    iloscUSD = "{0:.4f}".format(iloscUSD)
    print(f'ID USD wewnątrz funkcji: {id(kursUSD)}')
    return iloscUSD

print(f'\nKurs dolara: {kursUSD}')
pln = input('Podaj kwotę PLN jakie chcesz zamienić na USD: ')
usd = plnToUSD(float(pln))
print(f'ilosc {pln} PLN= {usd}USD')
print(f'Kurs dolara po wywołani funkcji: {kursUSD}')


plnToEur(1000)
