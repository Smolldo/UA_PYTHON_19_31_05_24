password = 'qwerty123'

if 'qwerty' in password or '123' in password:
    print('slabkiy parol')


# Зробити перевірку того, чи є число 3 в множині перших дев'яти простих чисел
# prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}

# isIn = 3 in prime_numbers
# print(isIn)

# Створити словник із наступними ключами (дивись нижче). Зробити перевірку чи є елемент 'age' 
# серед ключів словника та вивести інформацію, яка подана в Результаті.

user = {
    "name": "Bill",
    "surname": "Bosh",
    "age": 22
}

if "age" in user:
    print(f'{user["age"]} yers')

if len(password) < 12:
    print('password is to weak')

alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in alphabet:
    print(char)


# Задано словник, що містить відстані від Києва до обласних центрів. 
# Знайти обласний центр, найбільш віддалений від Києва.

cities = {
 'Київ' : 0, 
 'Вінниця' : 240, 
 'Харків' : 470, 
 'Ужгород' : 808, 
 'Львів' : 540, 
 'Житомир' : 120, 
 'Одеса' : 430
 }

distance = 0
far_city = ' '

for city, km in cities.items():
    if km > distance:
        distance = km
        far_city = city

print(f'MAX distance {far_city} = {distance}')

max_city = max(cities, key=cities.get)
print(f'{cities[max_city]} = {max_city}')


# Дано список міст, в яких працює Укрпошта та Нова Пошта. 
# Користувач вводить місто з клавіатури. Запропонувати користувачеві доставку поштовим оператором або 
# вивести повідомлення про неможливість доставки.

NP = ["Kyiv", "Snihurivka", 'Ternopil']
UP = ["Kyiv", "Snihurivka", "Odesa", 'Zhutomyr']

city = input('Enter city: ')

if city in NP and city in UP:
    print(f'dostupno i te i te')
elif city in NP:
    print('e nova poshta')
elif city in UP:
    print('e ukr poshta')
else:
    print('nema nichogo')

# Задано список туристичних ваучерів, в яких зазначено готель, прізвище власника, 
# кількість подорожуючих. Підрахувати, скільки туристів їдуть в кожен з готелів.
clients = [

 ['White House', 'Іванов', 3],

 ['Shelter', 'Іванова', 5], 

 ['Верховина', 'Іванова', 5], 

 ['Буковель', 'Іванова', 5]

]
dict = {}
for c in clients:
    print(f'do hotelu {c[0]} ide {c[2]} ludey')

dict[c[0]] = c[2]
