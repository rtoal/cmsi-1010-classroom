def investment_value(start, interest_rate, tax_rate, deposit, years):
    balance = start
    for _ in range(1, years + 1):
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
    return balance


def years_to_reach_goal(start, interest_rate, tax_rate, deposit, goal):
    years = 0
    balance = start
    while balance < goal:
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
        years += 1
    return years


print(investment_value(1000, 0.05, 0, 0, 10))  # should be 1628.89
print(investment_value(1000, 0.05, 0, 100, 10))  # should be 2886.68
print(investment_value(10000, 0.13, 0.25, 1000, 30))  # should be 319883.75
print(investment_value(1, 1, 0, 0, 20))  # should be 1048576.0

print(years_to_reach_goal(1000, 0.05, 0, 0, 2000))  # should be 15
print(years_to_reach_goal(1000, 0.05, 0, 100, 2000))  # should be 6
print(years_to_reach_goal(1000, 0.05, 0, 100, 5000))  # should be 18
print(years_to_reach_goal(10000, 0.13, 0.25, 1000, 100000))  # should be 19
print(years_to_reach_goal(1, 1, 0, 0, 1000000))  # should be 20
