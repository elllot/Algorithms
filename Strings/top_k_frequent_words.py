class Word(object):
    def __init__(self, count, label):
        self._count = count
        self._label = label
    
    def __lt__(self, other):
        if self._count == other._count:
            return self._label > other._label 
        return self._count < other._count
    
class Solution(object):
    
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if not words or not k: 
            return []
        counts = collections.Counter(words)
        heap = []
        for word in counts:
            wordObj = Word(counts[word], word)
            heapq.heappush(heap, wordObj)
            if len(heap) > k:
                heapq.heappop(heap)
        result_list = collections.deque()
        while heap:
            result_list.appendleft(heapq.heappop(heap)._label)                
        return list(result_list)