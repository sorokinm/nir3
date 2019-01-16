#!/usr/bin/env sage

import sys
from sage.all import *

# To count Hamming weight use .hamming_weight()
def get_vectors(dim):
    return VectorSpace(GF(2), dim)


def get_general_linear_group(dim):
    return GL(dim, GF(2))


def elementwise(operator, M, N):
    assert(M.parent() == N.parent())
    nc, nr = M.ncols(), M.nrows()
    A = copy(M.parent().zero_element())
    for r in xrange(nr):
        for c in xrange(nc):
            A[r,c] = operator(M[r,c], N[r,c])
    return A


def integral_branch_number(group_elem, dim):
    matrix = group_elem.matrix()
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


'''

if len(sys.argv) != 2:
    print("Usage: %s <n>" % sys.argv[0])
    print("Outputs the prime factorization of n.")
    sys.exit(1)
'''

#print(factor(sage_eval(sys.argv[1])))
param = 2
G = get_general_linear_group(param)

dim = 3

gl = get_general_linear_group(dim)

for g in gl:
    print(integral_branch_number(g, dim))
#print(gl[4])

'''
for gr in gp:
    print(branch_number(gr, dim))
'''