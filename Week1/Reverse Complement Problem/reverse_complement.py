#Reverse Complement Problem: Take the reverse complement of a string.
#Input: A DNA string "pattern"
#Output: The reverse complement of "pattern"
def get_reverse_complement(pattern):
	complement = {'A': 'T',
					'G': 'C',
					'T': 'A',
					'C': 'G'
				}
	reverse_complement = ""
	for nucleotide in pattern:
		reverse_complement = complement[nucleotide] + reverse_complement
	file = open('output.txt', 'w')
	file.write(reverse_complement)
	file.close()