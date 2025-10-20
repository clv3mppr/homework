tariffs = {
    'МТС': {
        'МТС': 0.0,  # Звонок на тот же оператор
        'Билайн': 1.5,
        'Мегафон': 1.8,
        'Теле2': 2.0
    },
    'Билайн': {
        'МТС': 1.6,
        'Билайн': 0.0,
        'Мегафон': 1.7,
        'Теле2': 2.1
    },
    'Мегафон': {
        'МТС': 1.7,
        'Билайн': 1.5,
        'Мегафон': 0.0,
        'Теле2': 2.2
    },
    'Теле2': {
        'МТС': 1.8,
        'Билайн': 1.9,
        'Мегафон': 2.0,
        'Теле2': 0.0
    }
}


def calculate_cost(call_cost, from_operator, to_operator):
    if from_operator in tariffs and to_operator in tariffs[from_operator]:
        tariff = tariffs[from_operator][to_operator]
        total_cost = call_cost * tariff
        return total_cost
    else:
        return None


def main():
    print("Доступные операторы: МТС, Билайн, Мегафон, Теле2")

    # Ввод стоимости разговора
    call_cost = float(input("Введите стоимость разговора за минуту: "))

    # Выбор оператора
    from_operator = input("Введите оператора, с которого звоните: ")
    to_operator = input("Введите оператора, на которого звоните: ")

    # Подсчет стоимости
    total_cost = calculate_cost(call_cost, from_operator, to_operator)

    if total_cost is not None:
        print(f"Стоимость разговора с {from_operator} на {to_operator}: {total_cost:.2f} руб.")
    else:
        print("Ошибка: некорректный ввод операторов.")


if __name__ == "__main__":
    main()