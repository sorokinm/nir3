#!/usr/bin/env sage

import sys
from sage.all import *

# To count Hamming weight use .hamming_weight()
def get_vectors(dim):
    return VectorSpace(GF(2), dim)


def get_general_linear_group(dim):
    return GL(dim, GF(2))


def integral_branch_number(group_elem, dim):
    matrix = group_elem
# .matrix() this is only for random matrices
    int_br_num = None
    for row in range(dim):
        for column in range(dim):
            tmp = map(operator.mul, matrix[row], matrix[:, column].transpose()[0])
            tmp = vector(GF(2), tmp).hamming_weight()
            if int_br_num is None or int_br_num > tmp:
                int_br_num = tmp
    return int_br_num


def branch_number(matrix, dim):
    vs = get_vectors(dim)
    # vs[0] == (0,0,0)
    min_br = None
    for v in vs:
        if v != vector(GF(2), [0] * dim):
            after_mult = (matrix * v).hamming_weight()
            prob_branch_number = v.hamming_weight() + after_mult
            if min_br is None or prob_branch_number < min_br:
                min_br = prob_branch_number
    return min_br


def convert_matrix_to_hex_comma_rep(matrix):
    res = ""
    for i in range(matrix.ncols()):
        res += hex(ZZ(list(rand_matrix[i]), base=2)) + ","
    return res[:-1]


'''

if len(sys.argv) != 2:
    print("Usage: %s <n>" % sys.argv[0])
    print("Outputs the prime factorization of n.")
    sys.exit(1)
'''

#print(factor(sage_eval(sys.argv[1])))

dim = 5

#gl = get_general_linear_group(dim)


#for i in range(2 ^ 4):
#    print(gl[randint(0, gl.order() - 1)])
#index = gl.order() - 1
#while index >= 0:
#    print(integral_branch_number(gl[index], dim))
#    index -= 1
#print(gl.order())

reviewed = set()
rand_suffix = str(randint(0, 100000))
matrix_file = open("rand_nonsingular_matrix" + str(dim) + ".txt" + rand_suffix, "w")
int_br_num_file = open("rand_nonsingular_matrix_int_br" + str(dim) + ".txt" + rand_suffix, "w")
br_num_file = open("rand_nonsingular_matrix_br" + str(dim) + ".txt" + rand_suffix, "w")

while True:
    rand_matrix = random_matrix(GF(2), dim, dim)
    if rand_matrix.is_singular() == False:
        str_matrix = convert_matrix_to_hex_comma_rep(rand_matrix)
        if str_matrix not in reviewed:
            reviewed.add(str_matrix)
            int_br = integral_branch_number(rand_matrix, dim)
            br_num = branch_number(rand_matrix, dim)
            matrix_file.write(str_matrix + "\n")
            int_br_num_file.write(str(int_br) + "\n")
            br_num_file.write(str(br_num) + "\n")
# random matrix

'''
for gr in gp:
    print(branch_number(gr, dim))
'''