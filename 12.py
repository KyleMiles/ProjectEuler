#!/usr/bin/env python3
 
from math import ceil, sqrt

limit = 1
currTri = 0

first = True
second = True

while first or second:
    currTri += limit

    helfDivisors = [i for i in range(1, ceil(sqrt(currTri))+1) if not currTri % i]

    if len(helfDivisors) >= 250:
        divisors = [i for i in range(1, currTri+1) if not currTri % i]
        print(currTri)
        print(divisors)
        break

    if not limit % 100:
        print(limit)

    limit += 1
