expenses_icomes = {
    'Monday' : {'expenses': 0, 'income':0},
    'Tuesday' : {'expenses': 0, 'income':0},
    'Wednsday' : {'expenses': 0, 'income':0},
    'Thursday' : {'expenses': 0, 'income':0},
    'Friday' : {'expenses': 0, 'income':0},
    'Saturday' : {'expenses': 0, 'income':0},
    'Sunday' : {'expenses': 0, 'income':0}
}


#получим ежедневные доходы и расходы пользователя


for day in expenses_icomes:
    expenses = int(input(f'Введите расходы  {day}: '))
    income = int(input(f'Введите доходы  {day} '))
    expenses_icomes[day]['expenses'] = expenses
    expenses_icomes[day]['income'] = income


#вычислаем общий баланс за неделю


total_expenses = sum(day['expenses'] for day in expenses_icomes.values())
total_income = sum(day['income'] for day in expenses_icomes.values())
balance = total_income - total_expenses


print('Общий баланс за неделю')
print(f'Расходы: {total_expenses}')
print(f'Доходы: {total_income}')
print(f'Баланс: {balance}')

