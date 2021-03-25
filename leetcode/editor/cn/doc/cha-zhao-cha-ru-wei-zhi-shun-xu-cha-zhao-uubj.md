### 解题思路
两种方法
1.顺序查找，找到第一个大于等于target的元素将其位置返回即可
2.折半查找（二分法），这里和上述思路一致，由于本题只需要查找到第一个大于等于target的位置，所以不需要特意判断nums[mid]是否同target相等

### 代码

```python3
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        #方法一：顺序查找，简单思路易懂但是效率很低
        n = len(nums)
        for i in range(n):
            if nums[i] >= target:
                return i
                break
        return n
            
        #方法二：二分法查找
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2# mid = left + (right - left)>>1  这种写法防止边界溢出
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid#######边界问题没有考虑清楚：起初写的是right=mid-1，忽略了中间元素与target相等的情况
        return left
```