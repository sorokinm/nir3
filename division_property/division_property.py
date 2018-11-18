import math
import numpy as np

def hamming_weight(number, bit_length):
    weight = 0
    for i in range(bit_length):
        weight += number & 0x1
        number >>= 1
    return weight


def count_division_property(input_set, bit_len=8):
    for i in range(2 ** bit_len):
        pass

def get_positional_functions(permutation):
    n = round(math.log(len(permutation), 2))
    result = []
    for i in range(n):
        shift = n - i - 1
        another_function = [ (permutation[j] >> shift) & 1 for j in range(len(permutation)) ]
        result.append(np.matrix(another_function).T)
    return result

if __name__ == "__main__":
    print(hamming_weight(0b101, 4))

    print(get_positional_functions([2, 3, 0, 1]))



