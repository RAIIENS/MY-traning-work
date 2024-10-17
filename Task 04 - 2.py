# "4th program"
# Дана строка '123.456'.
name = '123.456'
print(name)
print(type(name))
# Вывести на экран первую цифру после запятой - 4.
# преобразуем строку в дробное число
pop = float(name)
print(pop)
print(type(pop))
# выводим 4 в область целого числа
print(pop * 10)
# выводим на экран первую цифру после запятой
print(int(float(name) * 10) % 10)
