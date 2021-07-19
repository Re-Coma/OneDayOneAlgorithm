class TrieNode:
    child_nodes : dict
    is_key: bool
    data: str

    def __init__(self, data: str = None):
        self.child_nodes = {}
        self.data = data

class Trie:
    header: TrieNode
    length: int

    def __init__(self):
        self.header = TrieNode()
        self.length = 0

    def add(self, key: str, data: str) -> bool:
        cur_node = self.header

        # key Checking
        if len(key) == 0:
            raise ValueError("length is Zero")
        
        for char in key:
            if not char in cur_node.child_nodes:
                cur_node.child_nodes[char] = TrieNode()
            cur_node = cur_node.child_nodes[char]
        
        # 맨 끝에까지 갔으므로 중복 키 인지 확인
        if cur_node.data:
            return False
        else:
            cur_node.data = data
            self.length += 1
            return True

    def search(self, key: str) -> str:
        cur_node = self.header
        if len(key) == 0:
            raise ValueError("length is Zero")

        for char in key:
            if not char in cur_node.child_nodes:
                return None
            cur_node = cur_node.child_nodes[char]
        
        # 맨 끝에 까지 가서 데이터가 있는 지 확인
        return cur_node.data

    def search_key_automatic(self, key: str) -> list[str]:
        # 자동완성 검색
        result_list = []
        cur_node = self.header

        # Searching
        for char in key:
            if not char in cur_node.child_nodes:
                return []
            cur_node = cur_node.child_nodes[char]
        
        # 여기서부터 자동 검색(DFS 탐색)
        search_stack = []
        search_stack.append((cur_node, key))

        while search_stack:
            node, node_key = search_stack.pop()

            if node.data != None:
                result_list.append(node_key)

            for char in sorted(list(node.child_nodes.keys()), reverse=True):
                search_stack.append((node.child_nodes[char], node_key + char))

        return result_list


    def remove(self, key: str) -> None:
        cur_node = self.header

        def _remove(node, cur_len) -> bool:
            if cur_len == len(key):
                # 마지막 까지 도달한 경우
                # 단어가 맞는 지 확인
                return True if node.data else False
            else:
                char = key[cur_len]
                if char in node.child_nodes and _remove(node.child_nodes[char], cur_len + 1):

                    if cur_len + 1 == len(key):
                        # 자식 노드가 맨 마지막 검색단일 경우
                        if len(node.child_nodes[char].child_nodes) == 0:
                            del node.child_nodes[char]
                        else:
                            node.child_nodes[char].data = None
                        self.length -= 1
                        return True

                    else:
                        # 그렇지 않은 경우
                        if len(node.child_nodes[char].child_nodes) > 0 or node.child_nodes[char].data:
                            # 밑에 여러개의 노드를 갖고 있거나 그 노드 자체에 데이터가 존재하는 경우
                            # 그 부분부터 삭제를 하지 않는다/
                            return False
                        else:
                            del node.child_nodes[char].data
                            return True
                else:
                    return False
        _remove(cur_node, 0)

if __name__ == "__main__":
    trie = Trie()

    with open("words.txt") as f:
        for i in range(10000):
            r = f.readline()[:-1]
            trie.add(r, str(i))

    print(trie.search_key_automatic('ab'))