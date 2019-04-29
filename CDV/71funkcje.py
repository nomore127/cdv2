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