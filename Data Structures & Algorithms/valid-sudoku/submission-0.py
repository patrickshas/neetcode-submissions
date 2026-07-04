class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        subs = collections.defaultdict(set)

        for i in range (len(board)):
            for j in range (len(board[1])):
                print (board [i][j])
                
                if board [i][j] == ".":
                    continue
                elif (board [i][j] in columns [j] or 
                      board [i][j] in rows [i] or 
                      board [i][j] in subs [i//3, j//3]): 
                    return False

                columns [j].add(board [i][j])  
                rows [i].add(board [i][j])  
                subs [i//3, j//3].add(board [i][j])                

        return True