#!/usr/bin/env python3

"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp)

Return: The Hamming distance dH(s,t)
"""

with open("../datasets/rosalind_hamm.txt") as dataset:
    s, t = dataset.read().splitlines()

compare_list = [sc != tc for sc, tc in zip(s, t)]
print(sum(compare_list))