#!/usr/bin/env python3

"""
Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

with open("../datasets/rosalind_rna.txt") as dataset:
    t = dataset.read()
    t = t.replace("\n","")

u = t.replace("T", "U")
print(u)