#!/usr/bin/env python

from acme import Product
from random import randint, sample, uniform

ADJECTIVES = ['Awesome ', 'Shiny ', 'Impressive ', 'Portable ', 'Improved ']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []

    i = 0
    while (i < num_products):
        name = sample(ADJECTIVES, 1) + sample(NOUNS, 1)
        pro = Product(name=name,
                      price=randint(5,100),
                      weight=randint(5,100),
                      flammability=uniform(0.0,2.5))
        products.append(pro)
        i += 1

    return products

def inventory_report(products):
    names = len(products)

    for _ in products:
        price_list = []
        price_list.append(_.price)
        weight_list = []
        weight_list.append(_.weight)
        flammability_list = []
        flammability_list.append(_.flammability)

    mean_price = sum(price_list) / len(price_list)
    mean_weight = sum(weight_list) / len(weight_list)
    mean_flammability = sum(flammability_list) / len(flammability_list)

    print(f"ACME CORPORATION OFFICIAL INVENTORY REPORT\n"
          f"Unique product names: {names}\n"
          f"Average price: {mean_price}\n"
          f"Average weight: {mean_weight}\n"
          f"Average flammability: {mean_flammability}")

if __name__ == '__main__':
    inventory_report(generate_products())