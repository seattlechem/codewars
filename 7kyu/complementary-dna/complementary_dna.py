"""Complementary dna solution."""


def DNA_strand(dna):
    """Complementary dna will be returned."""
    src = ['A', 'T', 'C', 'G']

    # Split dna into array
    dna = dna.Split()

    if src[0] in dna:
        