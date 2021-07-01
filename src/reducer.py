#!/usr/bin/python
import sys

current_product = None
largest_basket_size = 0
sum_occurrences = 0
num_unique_products = 0

# input comes from STDIN (standard input)
for line in sys.stdin: # each line corresponds to a product

    product, basket_size, occurrences = line.split('\t', 2)

    if current_product == product:
        sum_occurrences += int(occurrences) # though we don't need to report it
        largest_basket_size = max(largest_basket_size, int(basket_size))

    else:
        num_unique_products += 1
        current_product = product
        sum_occurrences = int(occurrences) # though we don't need to report it
        largest_basket_size = max(largest_basket_size, int(basket_size))
