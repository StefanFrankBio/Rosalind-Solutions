#!/usr/bin/env python3

"""
Given: Two DNA strings s and t (each of length at most 1kbp).

Return: All locations of t as substring of s.
"""

with open("datasets/rosalind_subs.txt") as dataset:
    s, t = dataset.read().split()

pos = []
for i in range(1+len(s)-len(t)):
    if s[i:].startswith(t):
        pos.append(i+1)
print(*pos)