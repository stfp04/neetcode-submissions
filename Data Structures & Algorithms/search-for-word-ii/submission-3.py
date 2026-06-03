class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def _findPath(row, col, node, visit, result, w):
            c = board[row][col]
            if c not in node.children:
                return

            visit.add( (row, col) )
            w.append(c)

            cnode = node.children[c]
            if cnode.word:
                result.add( "".join(w) )


            i, j = row, col
            for k in [-1, 1]:
                if 0 <= j + k < COLS and \
                (i, j + k) not in visit:
                    _findPath(i, j + k, cnode, visit, result, w)

                if 0 <= i + k < ROWS and \
                (i + k, j) not in visit:
                    _findPath(i + k, j, cnode, visit, result, w)

            visit.remove( (row, col) )
            w.pop()

            return

        trie = Trie()
        for word in words:
            trie.add(word)

        ROWS, COLS = len(board), len(board[0])
        res = set()
        for i in range(ROWS):
            for j in range(COLS):
                c = board[i][j]
                if c not in trie.root.children:
                    continue
                _findPath(i, j, trie.root, set(), res, [])

        return list(res)