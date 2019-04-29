#Zasięg zmiennych, zmienne lokalne i globalne


#Precyzja liczby (zaokrąglenie do 3 miejsc po przecinku liczby
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
def plnToEur(value1):
    kursEur = 4.2927
    iloscEur = value1 / kursEur
    iloscEur = "{0:.4f}".format(iloscEur)
    print(iloscEur)

plnToEur(1000)