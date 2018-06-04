#!/usr/bin/env python3

count = 0

def rotate(num, shift):
    num = str(num)
    for _ in range(shift):
        num = num[-1] + num[:-1]
    return int(num)

def prime(num):
    for i in range(2, num//2+1):
        if not num % i:
            return False
    return True

for curr in range(1000001):
    if '2' in str(curr) or '4' in str(curr) or '5' in str(curr) or '6' in str(curr) or '8' in str(curr):
        continue

    isPrime = True

    for i in range(1, len(str(curr))+1):
        if not isPrime:
            continue
        isPrime = isPrime & prime(rotate(curr, i))

    if isPrime:
        print("circPrime:", curr)
        count += 1

print(count)
