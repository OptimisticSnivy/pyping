def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, row, N, solutions):
    if row == N:
        # Found a solution
        solutions.append([row[:] for row in board])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen
            board[row][col] = 1
            
            # Recur to place the rest of the queens
            solve_nqueens_util(board, row + 1, N, solutions)
            
            # Backtrack
            board[row][col] = 0

def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions

def print_solution(solution):
    for row in solution:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

# Example usage:
N = 4
solutions = solve_nqueens(N)
for idx, solution in enumerate(solutions):
    print("Solution", idx + 1)
    print_solution(solution)
