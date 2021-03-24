# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。 
# 
#  如果反转后整数超过 32 位的有符号整数的范围 [−231, 231 − 1] ，就返回 0。 
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 123
# 输出：321
#  
# 
#  示例 2： 
# 
#  
# 输入：x = -123
# 输出：-321
#  
# 
#  示例 3： 
# 
#  
# 输入：x = 120
# 输出：21
#  
# 
#  示例 4： 
# 
#  
# 输入：x = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  -2^31 <= x <= 2^31 - 1
#  
#  Related Topics 数学 
#  👍 2620 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        is_nav = True
        x2=str(x)
        if x >= 0:
            is_nav = False
        if is_nav:
            x2 = str(x)[1:]
            print(x2)
            x = - int(x2[::-1])
        else:
            print(x2)
            x=int(x2[::-1])
        return x if -2147483648 < x < 2147483647 else 0


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.reverse(1534236469))
