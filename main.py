'''
1. Дано список з рандомних елементів, тільки цифри але деякі передані у вигляді
стрічки. Через функцію map() з використанням анонімної функції- перетворити
типи елементів на протилежні.

2. Реалізувати таку ж дію (завдання №1) без використання анонімної функції але
з наявністю функції map().

3. Дано функцію, яка приймає рандомну кількість елементів та виводить на прінт
кортеж- довжина якого не більше ніж 10 елементів. Тут знадобиться перетворення
типів.
'''
lst = [1, 2, 3, 4, 5, '6', '7', '8']
lst_new = list(map(lambda arg: str(arg) if type(arg) == int else int(arg), lst))
print(lst_new)

def func(element):
    if type(element) == int:
        lst_new.append(str(element))
        return str(element)
    else:
        lst_new.append(int(element))
        return int(element)
lst_new = list(map(func, lst))
print(lst_new)

def func(*arg):
    lst = [i for i in range(10)]
    t = tuple(lst)
    return t
tuple = func()
print(tuple)