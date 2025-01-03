def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Initialize sets to track numbers in each row, column, and 3x3 box
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)  # key = (r//3, c//3)
    
    # Single pass through board
    for r in range(9):
        for c in range(9):
            # Skip empty cells
            if board[r][c] == ".":
                continue
                
            # If number already exists in row, column, or 3x3 square, return False
            if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or 
                board[r][c] in squares[(r//3, c//3)]):
                return False
            
            # Add number to sets
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])
    
    return True