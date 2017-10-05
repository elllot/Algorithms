"""
Given k sorted lists of integers of size n each, find the smallest range 
that includes at least element from each of the k lists. If more than one 
smallest ranges are found, print any one of them.
"""

import heapq

def smallestRange(lists):
    if len(lists) < 2: return 0 # can throw an error depending on implementation
    minHeap = []
    pointers = {i:0 for i in range(len(lists))}
    max_val = 0
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(minHeap, (lists[i][0], i))
            max_val = max(max_val, lists[i][0])
    min_range, range_ = float('inf'), []
    while len(minHeap) == len(lists):
        m, i = heapq.heappop(minHeap)
        r = max_val - m
        if r < min_range:
            min_range, range_ = r, [m, max_val]
        pointers[i] += 1
        if pointers[i] < len(lists[i]):
            val = lists[i][pointers[i]]
            heapq.heappush(minHeap, (val, i))
            max_val = max(max_val, val)
    return min_range, range_


if __name__ == '__main__':
    lists = \
        [
            [4, 7, 9, 12, 15],
            [0, 8, 10, 14, 20],
            [6, 12, 16, 30, 50]
        ]
    
    lists2 = \
        [
            [4,7],
            [1,2],
            [20,40]
        ]

    print(smallestRange(lists2))