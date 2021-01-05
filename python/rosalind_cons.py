#!/usr/bin/env python3

"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)
"""

with open("../datasets/rosalind_cons.txt") as dataset:
    fasta = dataset.read().split(">")

split_fasta = [s.splitlines() for s in fasta[1:]]
rows = ["".join(split_fasta[i][1:]) for i in range(len(split_fasta))]

nucs = ["A", "C", "G", "T"]
columns = []
counts = []
consensus = ""
for i in range(len(rows[0])):
    columns.append("".join([seq[i] for seq in rows]))
    counts.append([columns[-1].count(c) for c in nucs])
    consensus += nucs[counts[-1].index(max(counts[-1]))]

transposed_counts = list(map(list,zip(*counts)))
print(consensus)
for i in range(len(nucs)):
    print(nucs[i]+":",*transposed_counts[i])
