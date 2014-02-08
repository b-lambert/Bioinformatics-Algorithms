#Protein Translation Problem: Translate an RNA string into an amino acid string.
#Input: An RNA string "Pattern"
#Output: The translation of "Pattern" into an amino acid string "Peptide"

def translate(pattern):
    translation_table = create_translation_table()
    peptide = ""
    i = 0
    while i < len(pattern) - 2:
        current_substring = pattern[i:i+3]
        if translation_table[current_substring] == None:
            break
        peptide += translation_table[current_substring]
        i += 3
    return peptide

#Creates a table for translating RNA chunks into a peptide string
def create_translation_table():
    translation_table = {}
    with open('codon_table.txt') as lines:
        for line in lines:
            tokens = line.split()
            codon = tokens[0]
            if len(tokens) > 1:
                translation = tokens[1]
                translation_table[codon] = translation
            else:
                translation_table[tokens[0]] = None
    lines.close()   
    return translation_table
    
def test():
    RNA_string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    expected_peptide = "MAMAPRTEINSTRING"
    assert translate(RNA_string) == expected_peptide


if __name__ =="__main__":
    test()