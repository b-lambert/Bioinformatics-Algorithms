#Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
#Input: Two strings Pattern and Genome with an integer d
#Output: All positions where Pattern occurs in Genome with at most d mismatches.
def approximate_match(pattern, genome, mismatches):
	pattern_length = len(pattern)
	approximate_match_locations = []
	for i in range(0, len(genome) - pattern_length + 1):
		genome_slice = genome[i:i + pattern_length]
		mismatch_count = 0
		for index in range(0, pattern_length):
			if genome_slice[index] != pattern[index]:
				mismatch_count += 1
			if mismatch_count > mismatches:
				break
		if mismatch_count <= mismatches:
			approximate_match_locations.append(str(i))
	separator = ' '
	return(separator.join(approximate_match_locations))

def test():
	pattern = 'ATTCTGGA'
	genome = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
	mismatches = 3
	print(approximate_match(pattern, genome, mismatches))
	