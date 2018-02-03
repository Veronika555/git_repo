# Easy
#Number_1
# a = 5
# b = 6
# c = 9

# print(a,b,c)
#
# a = input('Введите переменную а')
# b = input('Введите переменную b')
# c = input('Введите переменную c')
#
# print(a,b,c)

#Number_2
# a = int(input('Введите число: '))
# print(a+2)

#Number_3
# age = int(input('Введите возраст: '))
#
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Извините, пользование данным ресурсом только с 18 лет')

# Normal
#Number_1
# while True:
#     a = int(input('Введите число больше нуля, но меньше 10: '))
#     if 0< a < 10:
#         print('a**2')
#         break
#     else:
#         print('Неверное число!')

#Number_2
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# a = a+b
# b = a-b
# a = a-b
#
# print(a,b)

# Hard
#Number_1
Name = input('Введите свое имя и фамилию: ')
Age = int(input('Введите свой возраст: '))
Weight = int(input('Введите свой вес: '))

if Age < 30 and 50 <= Weight < 120:
    print('Пациент в хорошем состоянии: ', Name, Age)
elif Age > 30 and 50 > Weight or Weight > 120:
    print('Необходимо вести правильный образ жизни: ')
elif Age >40 and 50 > Weight or Weight > 120:
    print('Требуется врачебный осмотр: ')
else:
    print('Знаете мой врачебный опыт ограничивается примитивной формулой основанной на весе и '
          'возрасте, приходите, когда будете подходить под эту формулу!')

#удалить после опробования



