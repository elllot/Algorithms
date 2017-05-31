def tour(r, c, board, move, target, X, Y):
	board[r][c] = move
	if move == target: return True
	for i in range(len(X)):
		R, C = r + X[i], c + Y[i]
		if 0 <= R < len(board) and 0 <= C < len(board[0]) and board[R][C] == -1:
			if tour(R, C, board, move + 1, target, X, Y): return True
	board[r][c] = -1
	return False

def knights_tour(n):
	board = [[-1] * n for i in range(n)]
	X = [2,1,-1,-2,-2,-1,1,2]
	Y = [1,2,2,1,-1,-2,-2,-1]
	cnt = n ** 2 - 1
	if tour(0, 0, board, 0, cnt, X, Y): return board

board = knights_tour(8)
for line in board:
	print(line)
