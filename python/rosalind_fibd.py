#!/usr/bin/env python3

"""
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""

with open("../datasets/rosalind_fibd.txt") as dataset:
    values = dataset.read().split()
    n, m = [int(value) for value in values]

pops = [0] * (m-1) + [1]
for _ in range(n-1):
    pops.append(pops[-1] + pops[-2])
    pops = [x-pops[0] for x in pops[1:]]

print(pops[-1])