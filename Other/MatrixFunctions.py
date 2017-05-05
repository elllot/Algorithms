from fractions import Fraction

"""
# Implementing common matrix functions without using a library (such as Numpy or Scipy)
"""

# utilizing zip and list comprehension to multipy two matrices
def matrix_mult(M, N):
	return [[sum(i * j for i, j in zip(r, c)) for c in zip(*N)] for r in M]

# returns an identity matrix of Fractions
def identity_matrix(size):
	return [[Fraction(int(i == j)) for i in range(size)] for j in range(size)]

# Utilizing LU Decomposition to get L & U matrices to use for 
# obtaining the inverse matrix of the matrix passed in
def lu_decomp(A): 
    n = len(A)
    # As per the formula U = A, L = I
    U, L = [r[:] for r in A], identity_matrix(n)
    for i in range(n-1): # for each column 
        for j in range(i+1, n): # for each row after i,i
            # compute the factor to eliminate following lines with
            L[j][i] = U[j][i] / U[i][i]
            # eliminating while updating the U matrix
            for k in range(i, n):
                U[j][k] -= L[j][i] * U[i][k]
    return L, U

def invert(A):
	n = len(A)
	# L, U through LU Decomposition
	L, U = lu_decomp(A)
	# the inverted matrix
	invrt = [[Fraction(0) for _ in range(n)] for _ in range(n)]
	# LZ = C (col in I) -> UX = Z
	for col in range(n):
		# Z will have 0's up to the current row due to the Identity matrix
		# having 0's until the current column. For row == col, add 1
		Z = [Fraction(0) for _ in range(col)] + [Fraction(1)]
		# Forward Substitution
		for row in range(col+1, n):
			val = Fraction(0)
			for i in range(col, row):
			    val += L[row][i] * Z[i]
			Z.append(-val)
		# X -> part of inverse matrix
		# since last row will only have the one value at the end ([-1][-1])
		# the X component for that one value then iterate from 2nd bottom up
		invrt[-1][col] = Z[-1] / U[-1][-1]
		# Backward Substitution
		for row in range(n-2, -1, -1): # from 2nd bottom up
			val = Fraction(0)
			for i in range(n-1, row, -1): # iterate over column
			    val += invrt[i][col] * U[row][i]
            # computing the row equation and inserting the value into the interverted matrix
			invrt[row][col] = (Z[row] - val) / U[row][row]
	return invrt