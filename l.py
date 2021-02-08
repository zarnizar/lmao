#!/bin/python

import time
import os
import sys

load = '-'
count = 0

for x in range (100):
    time.sleep(0.1)
    print(f'\r[•] MEMBUKA SISTEM {x}% [{load}]', end='', flush=True)
    count += 1
    if count == 3:
        count = 0
        load += '-'
print('\nSISTEM TERBUKA!')

