# Создадим пустой словать Capitals
Capitals = dict()

# Заполним его несколькими значениями
Capitals['Russia'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'

Countries = ['Russia', 'France', 'USA', 'Russia']

for x in Countries:
    # Для каждой страны из списка проверим, есть ли она в словаре Capitals
    if x in Capitals:
        print('Столица страны ' + x + ': ' + Capitals[x])
    else:
        print('В базе нет страны c названием ' + x)
