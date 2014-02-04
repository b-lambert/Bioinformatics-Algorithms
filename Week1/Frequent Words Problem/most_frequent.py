#Frequent Words Problem: Find the most frequent k-mers in a string.
#Input: A string Text and an integer k.
#Output: All most frequent k-mers in Text.

def most_frequent(text, k):
	kmer_count = {}
	for i in range(0, len(text) - (k + 1)):
		kmer = text[i:k]
		if kmer in kmer_count:
			kmer_count[kmer] += 1
		else:
			kmer_count[kmer] = 1
		k += 1
	#List containing the most frequently occuring k-mers
	max_kmers = []
	max = -1
	for kmer in kmer_count.keys():
		if kmer_count[kmer] > max:
			max = kmer_count[kmer]
			max_kmers = []
			max_kmers.append(kmer)
		elif kmer_count[kmer] == max:
			max_kmers.append(kmer)
	return max_kmers