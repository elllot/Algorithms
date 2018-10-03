from typing import List

def subsets(self, nums: List[int]):
    """
    takes in a list of distinct (sorted) ints and returns all possible non-duplicate
    subsets
    """
    res = []
    self.permute(0, [], nums, res)
    return res

def permute(self, idx, curr_list, nums, res):
    res.append(curr_list[:])
    for i in range(idx, len(nums)):
        curr_list.append(nums[i])
        self.permute(i + 1, curr_list, nums, res)
        curr_list.pop()