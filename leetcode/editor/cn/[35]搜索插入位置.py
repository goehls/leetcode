# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。 
# 
#  你可以假设数组中无重复元素。 
# 
#  示例 1: 
# 
#  输入: [1,3,5,6], 5
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [1,3,5,6], 2
# 输出: 1
#  
# 
#  示例 3: 
# 
#  输入: [1,3,5,6], 7
# 输出: 4
#  
# 
#  示例 4: 
# 
#  输入: [1,3,5,6], 0
# 输出: 0
#  
#  Related Topics 数组 二分查找 
#  👍 860 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i,n in enumerate(nums):
                if n == target:
                    return i
        else:
            i = len(nums)-1
            while i >=0:
                if nums[i] < target:
                    return i+1
                i -= 1
            return 0
    def searchInsert_1(self, nums: List[int], target: int) -> int:
        for i,n in enumerate(nums):
            if n >= target:
                return i
        return len(nums)

    def searchInsert_1(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)
        while L < R:
            mid = (L+R)//2
            if nums[mid] < target:
                L =  mid+1
            else:
                R = mid -1
        return L

# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
nums = [1,2,2,6]
target = 2
print(s.searchInsert(nums, target))

# print(5//2)
