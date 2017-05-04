from fractions import Fraction, gcd
from functools import reduce
import numpy as np

# generates R, Q matrices of the Markov Chain algorithm
def standardize(A):
    absorbing, other, totals = [], [], {}
    for i in range(len(A)):
    	s = sum(A[i]) # if sum of a row is 0, that state is terminal
    	if s == 0: 
    		absorbing.append(i)
    	else: 
    		other.append(i)
    		totals[i] = s
    # mapping each non-terminal state to a terminal state to generate the R matrix
    #R = [[Fraction(A[o][a], totals[o]) for a in absorbing] for o in other]
    R = [[ A[o][a] / totals[o] for a in absorbing] for o in other]
    # generating a cross matrix between non-terminal states for the Q matrix
    #Q = [[Fraction(A[o][ot], totals[o]) for ot in other] for o in other]
    Q = [[ A[o][ot] / totals[o] for ot in other] for o in other]
    return R, Q, absorbing, other

"""
# Given a n x n relational matrix, return F and FR matrices for the Markov Chain
# algorithm for calculating probabilities for absorbing states to answer interesting
# questions.
"""
def MarkovChain(m):
    # if there's only one state, it must be the terminal state
    # as the constraints indicate it's guaranteed all states 
    # can reach a terminal state
    if len(m) == 1: return [1,1]
    R, Q, absorbing, other = standardize(m)
    # I - Q (int(r==c) will be 1 diagonally across, which resembles an Identity matrix
    for r in range(len(Q)):
        for c in range(len(Q)):
            #Q[r][c] = Fraction(int(r==c)) - Q[r][c]
            Q[r][c] = float(r==c) - Q[r][c]
    # F = (I - Q) ^ -1
    #F = np.linalg.inv(np.array(Q, dtype=Fraction)) # inverting I - Q
    F = np.linalg.inv(np.array(Q))
    # F * R
    FR = np.matmul(F,R) # matrix muliplication. First row contains our target result set
    # We can use F and FR to answer markov chain related questions
    return F, FR, absorbing, other # absorbing and other will help us identify the order of the result set

T = int(input())
m = []
for t in range(T):
    m.append([int(c) for c in input().split()])
F, FR, absorbing, other = MarkovChain(m)