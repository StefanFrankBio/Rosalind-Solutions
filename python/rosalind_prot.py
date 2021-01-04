#!/usr/bin/env python3

"""
Given: A RNA string s corresponding to a strand of mRNA (of length at most 10 kbp)

Return: The protein string encoded by s.
"""
codon_dict = {"AAA":"K", "AAC":"N", "AAG":"K", "AAU":"N",
              "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T",
              "AGA":"R", "AGC":"S", "AGG":"R", "AGU":"S",
              "AUA":"I", "AUC":"I", "AUG":"M", "AUU":"I",
              "CAA":"Q", "CAC":"H", "CAG":"Q", "CAU":"H",
              "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P",
              "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R",
              "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L",
              "GAA":"E", "GAC":"D", "GAG":"E", "GAU":"D",
              "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A",
              "GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G",
              "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V",
              "UAA":"", "UAC":"Y", "UAG":"", "UAU":"Y",
              "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S",
              "UGA":"", "UGC":"C", "UGG":"W", "UGU":"C",
              "UUA":"L", "UUC":"F", "UUG":"L", "UUU":"F"}

with open("../datasets/rosalind_prot.txt") as dataset:
    s = dataset.read().replace("\n","")

protein = "".join([codon_dict[s[i:i+3]] for i in range(0,len(s),3)])
print(protein)