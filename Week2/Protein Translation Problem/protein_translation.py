def translate(pattern):
    translation_table = create_translation_table()
    peptide = ""
    peptide += translation_table[i] for i in range(0, i + len(pattern) - 2)
    return peptide
 
def create_translation_table():
    translation_table = {}
    with open('codon_table.txt') as lines:
        for line in lines:
            tokens = line.split()
            codon = tokens[0]
            if len(tokens) > 1:
                translation = tokens[1]
                translation_table[tokens[0]] = tokens[1]
            else:
                translation_table[tokens[0]] = None
    lines.close()   
    return translation_table = {}
    
def test():
    RNA_string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    print(translate(RNA_string))
    