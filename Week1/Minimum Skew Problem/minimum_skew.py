#Minimum Skew Problem: Find a position in a genome minimizing the skew.
#Input: A DNA string genome.
#Output: All integers minimizing skew(Genome) among all values from i from zero to length of the genome.

def minimum_skew(genome):
	skew = 0
	min = skew
	min_indices = []
	index = 0
	for char in genome:
		if char == 'C':
			skew -= 1
		elif char == 'G':
			skew += 1
		if skew < min:
			min = skew
			min_indices = [str(index + 1)]
		elif skew == min:
			min_indices.append(str(index + 1))
		index += 1
	return(' '.join(min_indices))

def test():
	genome = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
	assert minimum_skew(genome) == "11 24"