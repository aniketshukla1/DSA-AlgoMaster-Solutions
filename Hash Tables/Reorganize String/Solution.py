import heapq
from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = defaultdict(int)
        for char in s:
            hashmap[char] += 1

        heap = []
        for key in hashmap:
            heapq.heappush(heap, [-1 * hashmap[key], key])
        string = ""
        last_element = None
        while len(heap) > 0:
            popped_element = heapq.heappop(heap)
            if len(string) > 0 and string[-1] == popped_element[1]:
                return ""
            string += popped_element[1]
            popped_element[0] += 1
            if last_element != None and (-1 * last_element[0]) > 0:
                heapq.heappush(heap, last_element)
            last_element = popped_element
        if last_element != None and (-1 * last_element[0]) > 1:
            return ""
        elif last_element != None and (-1 * last_element[0]) == 1:
            if len(string) > 0 and string[-1] == last_element[1]:
                return ""
            else:
                string += last_element[1]
        return string
