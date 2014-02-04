def find_skew(genome):
	skew = 0
	skew_diagram = []
	skew_diagram.append(str(skew))
	for char in genome:
		if char == 'C':
			skew -= 1
		elif char == 'G':
			skew += 1
		skew_diagram.append(str(skew))
	return skew_diagram
	
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
			print(skew)
			min_indices = [str(index)]
		elif skew == min:
			min_indices.append(str(index))
		index += 1
	return(' '.join(min_indices))

def test():
	genome = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
	return find_skew(genome)