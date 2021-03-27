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
    return y_cash + b_cash
