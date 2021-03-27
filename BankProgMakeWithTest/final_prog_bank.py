import mymodule
from mymodule import check_float_number
from mymodule import check_int_number


def your_cash(payment, month):
    if month == 0:
        return payment
    cash = 0
    while month > 0:
        cash += payment
        month -= 1
    return cash


def bank_cash(payment, percent, month):
    cash = 0
    percent = percent / 100
    mount_payment = payment
    while month > 0:
        charges = payment * percent
        cash += charges
        payment += mount_payment + charges
        month -= 1
    return cash


def bank_cost(payment, percent, month):
    y_cash = your_cash(payment, month)
    b_cash = bank_cash(payment, percent, month)
    return y_cash, b_cash, y_cash + b_cash


def result():
    payment = ''
    percent = ''
    month = ''
    while not payment:
        payment = input("Введите ежемесячный взнос:")
        payment = check_float_number(payment)
        if not payment or payment < 0:
            payment = ''
            continue
    while not percent:
        percent = input("Введите ежемесячный банковский процент:")
        percent = check_float_number(percent)
        if not percent or percent < 0:
            percent = ''
            continue
    while not month:
        month = input("Введите срок накоплений в месяцах:")
        month = check_int_number(month)
        if not month or month < 0:
            month = ''
            continue
    res = bank_cost(payment, percent, month)
    print(f"Итоговая сумма в банке: {res[2]:.2f}")
    print("За все время...")
    print(f"Вы внесли: {res[0]:.0f}\nБанк вам начислил: {res[1]:.2f}")

result()
