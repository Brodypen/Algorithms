from test_framework import generic_test

# A bitwise question
# We are testing for parity, so a number like 1010 = 0, 1110= 1

# Parity is a way to test for errors in data storage or transmission.
# If parity does not match the expected value, then we know there is an error.

# Odd number = 1, Even number = 0

# Brute force is to check every bit, but we can do better.
# We can use the XOR operator to compare the bits.
# We can compare the bits in pairs, then compare the results of those pairs.

# Example: 1101 can be broken down to 11 and 01. The XOR of 11 is 0, and the XOR of 01 is 1.
# The XOR of 0 and 1 is 1, which is the correct parity.


def parity(x: int) -> int:
    num = 32
    while num >= 1:
        # print(num)
        x ^= x >> num
        num //= 2
    return x & 0x1



if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
