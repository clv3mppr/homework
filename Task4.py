def calculate_salary(sales):
    base_salary = 200
    if sales <= 500:
        commission = sales * 0.03
    elif sales <= 1000:
        commission = (500 * 0.03) + ((sales - 500) * 0.05)
    else:
        commission = (500 * 0.03) + (500 * 0.05) + ((sales - 1000) * 0.08)

    total_salary = base_salary + commission
    return total_salary

def main():
    sales_list = []
    for i in range(3):
        sales = float(input(f"Введите уровень продаж для менеджера {i + 1}: "))
        salary = calculate_salary(sales)
        sales_list.append((sales, salary))
        print(f"Зарплата менеджера {i + 1}: {salary:.2f}$")

    # Определяем лучшего менеджера
    best_manager_index = max(range(len(sales_list)), key=lambda i: sales_list[i][1])
    best_sales, best_salary = sales_list[best_manager_index]

    # Начисляем премию
    best_salary += 200
    print(f"\nЛучший менеджер: Менеджер {best_manager_index + 1} с продажами {best_sales}$")
    print(f"Зарплата лучшего менеджера с премией: {best_salary:.2f}$")

if __name__ == "__main__":
    main()