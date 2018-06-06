"""Other solutions."""


pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def DNA_strand(dna):
    """Create complementary pair list and then join."""
    return ''.join([pairs[x] for x in dna])


def other_DNA_strand(dna):
    """If statements."""
    # code here
    dnaComplement = ""
    for string in dna:
        if string == "A":
            dnaComplement += "T"
        elif string == "T":
            dnaComplement += "A"
        elif string == "G":
            dnaComplement += "C"
        elif string == "C":
            dnaComplement += "G"

    return dnaComplement
