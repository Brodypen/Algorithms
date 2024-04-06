from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # Okay, interesting question.
    # This question requres PRECOMPUTED_REVERSe which is every value for 2^16 reversed.
    # It's a lookup table. It's massive, I rather not copy it.

    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE) |
            PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE) |
            PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE |
            PRECOMPUTED_REVERSE[(x >> (3 * MASK_SIZE)) & BIT_MASK])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
