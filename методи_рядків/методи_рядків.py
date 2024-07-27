# # str.count(substring, start, end)

a = 'po po po popopoposdfsdfsdfpopo'
print(a.count('po', 6, 12))

b = 'крісло і диван, стіл і книга'
print(b.count(' і '))

# регістри lower(), upper(), capitalize(), swapcase(), title()

c = 'FdGGdFsfsGDFG'
print(c.lower())
print(c.upper())

d = 'lorem ipsum dolores'
print(d.capitalize())

f = ' A b C d E f G' #a B c D e F g
print(f.swapcase())

print(d.title())


# # пошук у рядку
# #  str.find(substr, start, end)

s = 'hello wowowowowowoworldwo'

print(s.find('wo'))
print(s.find('q'))

# rfirnd()
print(s.rfind('wo'))

S = 'Big, Bigger, Biggest' # Big

print(S.rfind('Big')) # індекс останнього входження підрядка Big
print(S.count('Big')) # загальна кількість Big
print(S.find('Big')) # індекс першого входження Big



# # Ввести довільне повідомлення з клавіатури. 
# # Якщо в повідомленні трапляються слова «купити», «продати», «реклама», 
# # то помітити це повідомлення як спам.

spam_words  = ["купити", "продати", "реклама"]

inp = input()
ok = -1
is_spam = False

for i in spam_words:
    if inp.find(i)  != ok:
        is_spam = True
        break

txt = 'spm detected' if is_spam else 'no spam'
print(txt)


s = 'lorem, ipsum, dolores. dolores, ipsum lorem'

s = s.split(', ')

print(s)

# Ввести довільне речення з клавіатури і порахувати кількість слів.

txt = input('Enter: ').split()
txt = txt.split()
print(len(txt))

# Нові рядки на основі рядків      .join(розділювач)

text = ['hello worl', '123rusUa123', 'world of pain']

text = '. '.join(text)
print(text)

t = 'all dogs can bark'
t1 = t.replace('dogs', 'cats')
print(t1)

d = {
    ord('з'): 'привіт, я Халк',
    ord('ж'): 'zh',
    ord('г'): 'h'
}

translated = 'зюзюзу'.translate(d)
print(translated)

age = 25
print(f'мені {age} років.')

#   %

s1 = 'Привіт, мене звати %r. мені %a років' % ("Михайло", 25)
print(s1)

# .format()

s2 = 'Мене звати {1}. Мені {0}. I live in {2}'.format('M', 25, 'SNK')
print(s2)


# специфікація

print('pi: {:.2f}'.format(3.1415926))

a = 5 / 3
print('a = {:.7f}'.format(a))

print('"{}", "{:+}", "{:-}", "{: }"'.format(1,2,-3,4))


# як вирівняти положення елемента і чим (якими символами) доповнити:
print('-' * 34)
print("|{:^10}|{:^10}|{:^10}|".format('left', 'center', 'right'))
print('-' * 34)
