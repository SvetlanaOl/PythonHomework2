#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

number = input("Введите число: ")
i = 0
for elem in number:
    if elem.isdigit():
        i += int(elem)

print(i)