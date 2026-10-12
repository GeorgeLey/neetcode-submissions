class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            Understand:
            - Output: boolean of whether or not the matrix is a valid sudoku board
            - input: 9x9 matrix where each value is a number 1-9 or a . representing no value
            - Constraint: none
            - Edge cases: full board, empty board, 

            Match: array
            Plan:
            - create a dictionaries for cols, rows, and each square where the key is the row index and the value is a set
            - for the square dictionary each key is equivalent to (r //3, c //3) so that we can have an identifier for a square on the board
            - Then loop thru every square in the board and
                - if "." continue
                - check if it already exists in the 3 dicts if it does return false
                    - add the value to each hashset if not
            - return true at the end
        """


        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True



        