def investment_value(start, interest_rate, tax_rate, deposit, years):
    balance = start
    for _ in range(1, years + 1):
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
    return balance


print(
    investment_value(
        start=1000, interest_rate=0.13, tax_rate=0.25, deposit=1000, years=30))
