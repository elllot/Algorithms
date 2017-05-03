def heightFromParents(arr):
    if not arr: return 0
    maxHeight = -1
    heights = {}
    for i in range(len(arr)):
        res = getHeight(i, arr, heights)
        if res > maxHeight: maxHeight = res
    return res
    
def getHeight(index, arr, heights):
    if arr[index] == -1: return 1
    if index in heights: return heights[index]
    height = getHeight(arr[index], arr, heights) + 1
    heights[index] = height
    return height

print(heightFromParents([1,5,5,2,2,-1,3]))