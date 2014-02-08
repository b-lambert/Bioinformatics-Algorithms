import operator

def find_mismatch(genome, window, mismatch):
    kmer_count = {}
    replacements = {'A': 'CTG', 'C': 'ATG', 'G': 'CTA', 'T': 'CGA'}
    for i in range(0, len(genome) - window + 1):
        d = 0
        slice = genome[i:i + window]
        print(slice)
        current_kmers = []
        next_kmers = []
        current_kmers.append(slice)
        while d < mismatch:
            for kmer in current_kmers:
                if mismatch == d:
                    break
                for j in range(0, window - 1):
                    for char in replacements[slice[j]]:
                        temp_slice = kmer
                        temp_slice = list(temp_slice)
                        temp_slice[j] = char
                        temp_slice = "".join(temp_slice)
                        current_kmers.append(temp_slice)
                d += 1
                print(current_kmers)
                current_kmers = list(set(current_kmers))
        for kmer in current_kmers:
            if kmer not in kmer_count.keys():
                kmer_count[kmer] = 1
            else:
                kmer_count[kmer] += 1
    print(kmer_count)
    print(max(kmer_count.iteritems(), key=operator.itemgetter(1))[0])
    
def main():
    genome = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    window = 4
    mismatch = 1
    find_mismatch(genome, window, mismatch)

if __name__ =="__main__":
    main()

