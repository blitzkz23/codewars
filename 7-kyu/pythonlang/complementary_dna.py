# Complementary DNA [https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python]
def DNA_strand(dna):
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    result = ''
    for nucleotide in dna:
        result += complements[nucleotide]
    return result

# People one liner
def DNA_strand2(dna):
    return dna.translate(dna.maketrans("ATCG", "TAGC"))