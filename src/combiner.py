#!/usr/bin/python
import sys

current_product = None
largest_basket_size = 0
sum_occurrences = 0

# input comes from STDIN (standard input)
for line in sys.stdin: # each line corresponds to a product


    product, basket_size, occurrences = line.split('\t', 2)

    if current_product == product:
        sum_occurrences += int(occurrences)
        largest_basket_size = max(largest_basket_size, int(basket_size))

    else:

        if current_product:
            print '{0}\t{1}\t{2}'.format(current_product, largest_basket_size, 
                                         sum_occurrences)
        current_product = product
        sum_occurrences = int(occurrences)
        largest_basket_size = int(basket_size)

if current_product == product:
    print '{0}\t{1}\t{2}'.format(current_product, largest_basket_size, 
                                 sum_occurrences)
