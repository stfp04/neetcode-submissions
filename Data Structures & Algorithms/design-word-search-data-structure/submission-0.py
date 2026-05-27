class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        queue = deque()

        i = 0
        if word[i] == '.':
            for child in self.head.children.values():
                queue.append(child)
        elif word[i] in self.head.children:
            queue.append(self.head.children[word[i]])
        i += 1

        while queue and i < len(word):
            c = word[i]
            for _ in range(len(queue)):
                node = queue.popleft()

                if c == '.':
                    for child in node.children.values():
                        queue.append(child)
                elif c in node.children:
                    queue.append(node.children[c])

            i += 1

        if not queue:
            return False
        
        for node in queue:
            if node.word:
                return True
        return False




