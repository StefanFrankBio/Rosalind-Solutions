#!/usr/bin/env python3

"""
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

with open("../datasets/rosalind_revc.txt") as dataset:
    s = dataset.read()

comp_dict = str.maketrans("ACGT", "TGCA", "\n")
sc = s[::-1].translate(comp_dict)
print(sc)