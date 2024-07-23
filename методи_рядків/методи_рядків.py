# str.count(substring, start, end)

a = 'po po po popopoposdfsdfsdfpopo'
# print(a.count('po', 6, 12))

b = 'крісло і диван, стіл і книга'
# print(b.count(' і '))

# регістри lower(), upper(), capitalize(), swapcase(), title()

c = 'FdGGdFsfsGDFG'
# print(c.lower())
# print(c.upper())

d = 'lorem ipsum dolores'
# print(d.capitalize())

f = ' A b C d E f G' #a B c D e F g
# print(f.swapcase())

# print(d.title())


# пошук у рядку
#  str.find(substr, start, end)

s = 'hello wowowowowowoworldwo'

# print(s.find('wo'))
# print(s.find('q'))

# rfirnd()
# print(s.rfind('wo'))

S = 'Big, Bigger, Biggest' # Big

# print(S.rfind('Big')) # індекс останнього входження підрядка Big
# print(S.count('Big')) # загальна кількість Big
# print(S.find('Big')) # індекс першого входження Big



# Ввести довільне повідомлення з клавіатури. 
# Якщо в повідомленні трапляються слова «купити», «продати», «реклама», 
# то помітити це повідомлення як спам.

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

