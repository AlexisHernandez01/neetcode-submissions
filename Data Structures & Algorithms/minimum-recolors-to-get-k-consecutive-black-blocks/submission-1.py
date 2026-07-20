class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        minMoves = k
        currMoves = 0
        window = list()
        L = 0

        for R in range(len(blocks)):
            
            window.append(blocks[R])
            
            if blocks[R] == 'W':
                currMoves += 1

            if len(window) == k:
                minMoves = min(minMoves, currMoves)
                window.remove(blocks[L])
                if blocks[L] == 'W':
                    currMoves -= 1
                L += 1

        return minMoves
            