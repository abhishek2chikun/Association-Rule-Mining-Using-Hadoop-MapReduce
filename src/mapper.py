#!/usr/bin/python
import sys

# dicitionary with unique products as keys
unique_product = {}


# input comes from STDIN (standard input)
for line in sys.stdin:
    basket = line.split() # each line is a record 
    basket_size = len(basket) # its size is the number value
    for product in basket:
        # If new value is found, add to dictionary
        if product not in unique_product.keys():
            # Value for each key is a duple
            unique_product[product] = [basket_size, 1]

        else: # if already included

            unique_product[product][0] = max(unique_product[product][0], 
                                             basket_size)
            # Increment number 
            unique_product[product][1] += 1


for product in unique_product.keys():
    print '{0}\t{1}'.format(product,'\t'.join(map(str, 
                                                  unique_product[product])))
