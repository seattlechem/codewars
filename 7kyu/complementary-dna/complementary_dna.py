"""Complementary dna solution."""


def DNA_strand(dna):
    """Change dna to complimentary pairs."""
    src = ['A', 'T', 'C', 'G']

    # Split dna into array
    dna = list(dna)

    for i in range(len(dna)):
        if dna[i] == src[0]:
            dna[i] = src[1]

        elif dna[i] == src[1]:
            dna[i] = src[0]

        elif dna[i] == src[2]:
            dna[i] = src[3]

        else:
            dna[i] = src[2]

    str_dna = ''.join(map(str, dna))

    return str_dna
