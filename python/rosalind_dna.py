#!/usr/bin/env python3

"""
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', 'T' occur in s.
"""

with open("../datasets/rosalind_dna.txt") as dataset:
    s = dataset.read()
    s = s.replace("\n", "")

counts = [s.count(c) for c in sorted(set(s))]
print(*counts)