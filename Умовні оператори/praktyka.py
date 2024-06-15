# координати

x = -3
y = -5

if x >= 0 and y >= 0:
    print('1 chvert')
elif x < 0 and y >= 0:
    print('2 chvert')
elif x < 0 and y < 0:
    print('3 chvert')
elif x >= 0 and y < 0:
    print('4 chvert')
else:
    print('ne nalezhut')

# Дано ціле число. Якщо воно є позитивним, додати до нього 1; інакше не змінювати його. Вивести отримане число.
a = 0

if a > 0: # додатнє(позитивне)
    a += 1 # a = a + 1
    print(a)
elif a < 0:
    # a-=2
    print(a)
else:
    print("число є 0")

# Дано три цілих числа. Знайти кількість позитивних чисел у даному наборі.

a,b,c = -2,3,-4

count = 0

if a > 0:
    count += 1 # count = count + 1
if b > 0:
    count += 1
if c > 0:
    count +=1
print(count)

# Дано три цілих числа. Знайти кількість позитивних та кількість негативних чисел у даному наборі.
a,b,c = -2,-3,-4

poz_num = 0
neg_num = 0

if a > 0:
    poz_num +=1
else:
    neg_num += 1
if b > 0:
    poz_num +=1
else:
    neg_num += 1
if c > 0:
    poz_num +=1
else:
    neg_num += 1
print(f'amount of poz nums = {poz_num}, neg nums = {neg_num}')

# Магазин дає знижку 10%, якщо покупець здійснить покупку більше ніж на 1000 грн. Завдання: Запитати у користувача кількість купленого товару. Нехай одна одиниця товару коштує 100 грн. Перевірити та порахувати загальну суму для користувача.
discount = 0.1 # знижка в 10%
disc_price = 1000 # сума, яка треба для отримання знижки

pcs = int(input('how many?: ')) # скільки товару купуємо
price_for_pcs = 100 # ціна за 1 шт товару

total = price_for_pcs * pcs # загальна вартість

if total > disc_price: # чи буде знижка
    total -= total * discount # віднімання знижки від загальної суми
    print(f'vasha cina zi znuzhkoju =  {total}')
else:
    print(f'vasha cina =  {total}')


# Арифметичні дії над числами пронумеровані таким чином: 1 — додавання, 2 — віднімання, 3 — множення, 4 — ділення. Дано номер дії N (ціле число в діапазоні 1–4) та дійсні числа A та B (B не дорівнює 0). Виконати над числами вказану дію та вивести результат.
n = int(input('vvedu chisla vid 1 do 4: '))
a = int(input('vvedi a: '))
b= int(input('vvedi b, b != 0: '))

if n == 1:
    print(a+b)
elif n ==2:
    print(a - b)
elif n == 3:
    print(a * b)
elif n == 4:
    print(a / b)

# Оголосити змінні х та у (числа). За допомогою умовного оператора перевірити яке число більше.
x = 3
y = 4

bigger = x if x > y else y # тернарний оператор
print(bigger)
