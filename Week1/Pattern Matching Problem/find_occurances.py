#Pattern Matching Problem: Find all occurances of a pattern in a string.
#Input: Two strings, pattern and genome
#Output: All starting positions where Pattern appears as a substring of Genome.

def find(pattern, string):
	occurrences = []
	length = len(pattern)
	for i in range(0, len(string) - (length + 1)):
		slice = string[i:i + length]
		print(slice)
		if slice == pattern:
			occurrences.append(str(i))
	arr = ' '.join(occurrences)
	file = open('occurrences.txt', 'w')
	file.write(arr)
	file.close()