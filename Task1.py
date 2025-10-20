number = int(input("Введите число от 1 до 100"))
if number % 3 == 0:
    print('Fizz')
if number % 5 == 0:
    print('Buzz')
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
if number % 3 != 0 and number % 5 != 0:
    print(number)
else:
    print("Ошибка ввода операции")