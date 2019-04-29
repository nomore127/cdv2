#Przekazywanie argumentów przez referencje

def show(name):
    print(f'Przed modycfikacją: {name}')
    name[0] = 'Beata'
    name[1] = 'Barbara'
    name[2] = 'Bogdan'
    print(f'Po modycfikacją: {name}')
    print(f'Po modycfikacją: {id(name)}')


data = ['Anna', 'Agnieszka', 'Andrzej']

print(f'Przed wywyołaniem funkcji show: {data}')
print(f'Id obiektu show: {id(data)}')

show(data)

print(f'Przed wywyołaniem funkcji show: {data}')

####################### słownik #######################

data1 = {
    0:'Artur',
    1:'Andrzej'
}

print(f'Przed wywyołaniem funkcji show: {data1}')
show(data1)

####################### Przekazywanie armugentów przez wartość #######################
print('\n########## Przekazanie przez wartość')

def show1(city):
    print(f'Przed modycfikacją: {city}')
    city[0] = 'Berlin'
    city[1] = 'Bukareszt'
    print(f'Po modycfikacją: {city}')
    print(f'Po modycfikacją: {id(city)}')

miasto = ['Poznań','Gniezno']

print(f'Przed wywyołaniem funkcji show1: {miasto}')
print(f'Id obiektu show: {id(miasto)}')
show1(list(miasto))
print(f'Po wywyołaniem funkcji show1: {miasto}')

####################### Słownik #######################

def show2(abecadlo):
    print(f'Przed modycfikacją: {abecadlo}')
    abecadlo[0] = 'A'
    abecadlo[1] = 'B'
    abecadlo[2] = 'C'
    abecadlo[3] = 'D'
    abecadlo[4] = 'E'
    abecadlo[5] = 'F'
    print(f'Po modycfikacją: {abecadlo}')
    print(f'Po modycfikacją: {id(abecadlo)}')

asd = ['F','E','D','C','B','A']

print(f'Przed wywyołaniem funkcji show2: {asd}')
print(f'Id obiektu show: {id(asd)}')
show2(list(asd))
print(f'Po wywyołaniem funkcji show2: {asd}')