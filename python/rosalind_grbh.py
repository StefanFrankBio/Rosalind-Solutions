#!/usr/bin/env python3

"""
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
"""

with open("../datasets/rosalind_grbh.txt") as dataset:
    fasta = dataset.read().split(">")

split_fasta = [s.splitlines() for s in fasta[1:]]
headers = [s[0] for s in split_fasta]
seqs = ["".join(split_fasta[i][1:]) for i in range(len(split_fasta))]

adj_list = []
for i, seq1 in enumerate(seqs):
    for j, seq2 in enumerate(seqs):
        if seq1 != seq2:
            if seq1[-3:] == seq2[:3]:
                adj_list.append(f"{headers[i]} {headers[j]}")

print(*adj_list, sep="\n")
