# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 103 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  只会存在一个有效答案 
#  
#  Related Topics 数组 哈希表 
#  👍 10582 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        """
        暴力破解法
        :param nums:
        :param target:
        :return:
        """
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
        return []
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1.注意到方法一的时间复杂度较高的原因是寻找 target - x 的时间复杂度过高。因此，我们需要一种更优秀的方法，能够快速寻找数组中是否存在目标元素。如果存在，我们需要找出它的索引。
        2.使用哈希表，可以将寻找 target - x 的时间复杂度降低到从 O(N)O(N) 降低到 O(1)O(1)。
        3.这样我们创建一个哈希表，对于每一个 x，我们首先查询哈希表中是否存在 target - x，然后将 x 插入到哈希表中，即可保证不会让 x 和自己匹配。

        :param nums:
        :param target:
        :return:
        """
        hashtable ={}
        for i,num in enumerate(nums):
            if target-num in hashtable:
                return [i,hashtable[target-num]]
            hashtable[nums[i]] = i
        return []

# leetcode submit region end(Prohibit modification and deletion)
