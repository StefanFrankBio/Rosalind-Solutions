#!/usr/bin/env python3

"""
Given: Three positive integers k, m, n representing a population k + m + n
organisms: k individuals are homozygous dominant for a factor, m are
heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will
produce an individual possessing a dominant allele (and thus displaying the
dominant phenotype). Assume that any two organisms can mate.
"""

with open("../datasets/rosalind_iprb.txt") as dataset:
    values = dataset.read().split()
    k, m, n = [int(v) for v in values]

pop = sum([k, m, n])
proba = 1-(m*(m-1)*0.25+m*n+n*(n-1))/(pop*(pop-1))
print(proba)