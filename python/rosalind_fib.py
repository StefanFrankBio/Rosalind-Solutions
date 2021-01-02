#!/usr/bin/env python3

"""
Given: Positive integers n smaller or equal to 40 and
k smaller or equal to 5

Return: The total number of rabbit pairs that will be present after
n months. If we begin with 1 pair and in each generation, every pair
of reproduction-age rabbits produces a litter of k rabbit pairs.
"""

with open("../datasets/rosalind_fib.txt") as dataset:
    values = dataset.read().split()
    n, k = [int(value) for value in values]

f1 = f2 = 1
for _ in range(2,n):
    f1, f2 = f2, f1*k+f2

print(f2)