from operator import itemgetter
from collections import Counter
from itertools import groupby
import matplotlib.pyplot as plt
import csv

with open('farmers_markets.csv', 'r') as file:
    markets = [row for row in csv.DictReader(file)]


def california_market_names():
    return [m['MarketName'] for m in markets if m['State'] == 'California']


def alaska_market_names():
    return [m['MarketName'] for m in markets if m['State'] == 'Alaska']


def market_names_in_state(state):
    return [m['MarketName'] for m in markets if m['State'] == state]


def market_counts_by_state_directly():
    state_counts = {}
    for m in markets:
        state = m['State']
        state_counts[state] = state_counts.get(state, 0) + 1
    return state_counts


def market_counts_by_state_with_groupby():
    # Sort markets by 'State' for groupby to work correctly
    sorted_markets = sorted(markets, key=itemgetter('State'))
    return {state: len(list(group)) for state, group in groupby(sorted_markets, key=itemgetter('State'))}


def market_counts_by_state_with_counter():
    return Counter(m['State'] for m in markets)


def markets_selling_nuts():
    return [m for m in markets if m['Nuts'] == 'Y']


def markets_in_maine_selling_nuts_but_not_seafood():
    return [m for m in markets if m['State'] == 'Maine' and m['Nuts'] == 'Y' and m['Seafood'] == 'N']


def markets_with_you_tube_west_of_100():
    return [
        (m['MarketName'], m['street'], m['city'], m['zip'])
        for m in markets
        if float(m['x']) < -100 and m['Youtube'] != ''
    ]


def plot_market_histogram():
    state_counts = market_counts_by_state_with_counter()
    plt.bar(state_counts.keys(), state_counts.values())
    plt.xticks(rotation=90)
    plt.xlabel('State')
    plt.ylabel('Number of Farmers Markets')
    plt.title('Farmers Markets by State')
    plt.tight_layout()
    plt.show()


# plot_market_histogram()

mc1 = market_counts_by_state_directly()
mc2 = market_counts_by_state_with_groupby()
mc3 = market_counts_by_state_with_counter()

print(type(mc1))
print()
print(type(mc2))
print()
print(type(mc3))
print()


assert mc1 == mc2 and mc2 == mc3
print("All good")

print(markets_with_you_tube_west_of_100())
print(markets_selling_nuts())
print(markets_in_maine_selling_nuts_but_not_seafood())

plot_market_histogram()
