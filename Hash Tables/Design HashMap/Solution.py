class ListNode:
    def __init__(self, key=None, value=None, nxt=None):
        self.key = key
        self.value = value
        self.nxt = nxt


class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.nxt:
            if cur.nxt.key == key:
                cur.nxt.value = value
            cur = cur.nxt
        cur.nxt = ListNode(key=key, value=value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.nxt
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur and cur.nxt:
            if cur.nxt.key == key:
                cur.nxt = cur.nxt.nxt
                return
            cur = cur.nxt


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
