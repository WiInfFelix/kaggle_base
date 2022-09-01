from dataclasses import dataclass
import numpy as np

np.random.seed(42)

@dataclass
class Item:
    '''Class representing an Item'''
    id: int
    name: str
    value: float


@dataclass
class ItemPurchase:
    '''ItemPurchase represents the purchase of a single item '''
    id: int
    item_id: int
    amount: int


@dataclass
class Transaction:
    '''Transaction bundles together purchased items in single Transactions'''
    id: int
    item_purchases: list[ItemPurchase]


@dataclass
class Location:
    '''Location represents '''
    id: int
    name: str
    transactions: list[Transaction]


wine1 = Item(1, "Rotwein edel", 12.0)
wine2 = Item(2, "Weißwein edel", 8.0)
wine3 = Item(3, "Merlotte", 15.0)

wines = [wine1, wine2, wine3]

location1 = Location(1, "Hamburg", [])
location2 = Location(2, "Berlin", [])
location3 = Location(3, "Düsseldorf", [])

locations = [location1, location2, location3]

for i in range(1, 10001):
    trans = Transaction(i, [])

    for y in range(len(wines)-1):
        amount_purchased = np.random.randint(4)
        item_pur = ItemPurchase(i, y, amount_purchased)
        trans.item_purchases.append(item_pur)