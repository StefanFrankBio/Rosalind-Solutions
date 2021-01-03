#!/usr/bin/env python3

"""
Given: At most 10 DNA strings in FASTA format (of length at most 1kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0,001 in all
decimal answers unless otherwise stated.
"""

with open("../datasets/rosalind_gc.txt") as dataset:
    fasta = dataset.read().split(">")

split_fasta = [s.splitlines() for s in fasta[1:]]
headers = [s[0] for s in split_fasta]
seqs = ["".join(split_fasta[i][1:]) for i in range(len(split_fasta))]
gc_contents = [(s.count("C") + s.count("G")) / len(s) * 100 for s in seqs]
idx_max = gc_contents.index(max(gc_contents))
print(f"{headers[idx_max]}\n{gc_contents[idx_max]}")