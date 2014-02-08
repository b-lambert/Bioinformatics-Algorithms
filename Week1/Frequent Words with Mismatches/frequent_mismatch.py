from itertools import combinations
from collections import Counter

# Hamming distance function
def hamming_distance(s, t):
    if len(s) != len(t):
        raise ValueError("Hamming distance is undefined for sequences of different lengths.")
    return sum( s[i] != t[i] for i in range(len(s)) )

# Main function
# - k is for k-mer
# - m is max hamming distance
def hamming_kmer(genome, k, m):
    # Enumerate all k-mers
    kmers = [ genome[i:i+k] for i in range(len(genome)-k + 1) ]

    # Compute initial counts
    initcount  = Counter(kmers)
    kmer2count = dict(initcount)

    # Compare all pairs of k-mers
    for kmer1, kmer2 in combinations(set(kmers), 2):
        # Check if the hamming distance is small enough
        if hamming_distance(kmer1, kmer2) <= m:
            # Increase the count by the number of times the other
            # k-mer appeared originally
            kmer2count[kmer1] += initcount[kmer2]
            kmer2count[kmer2] += initcount[kmer1]

    return kmer2count


# Count the occurrences of each mismatched k-mer\
def test():
    genome = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    kmer2count = hamming_kmer(genome, 4, 1)
    # Print the max k-mer and its count
    print(max(kmer2count.items()))
    # Output => ('ATGC', 5)