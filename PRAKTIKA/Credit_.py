income = int(input("Введите свой ежемесячный доход"))
credit_rating = int(input("Введите свой кредитный рейтинг"))

if income >= 5000:
    if credit_rating >=7:
        print('Вам одобрено')
    else:
        print('Вам не одобрено')
else:
    print('Вам не одобрено')