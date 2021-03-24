# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "()"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "()[]{}"
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "(]"
# 输出：false
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "([)]"
# 输出：false
#  
# 
#  示例 5： 
# 
#  
# 输入：s = "{[]}"
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 仅由括号 '()[]{}' 组成 
#  
#  Related Topics 栈 字符串 
#  👍 2263 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        """
        栈的后进先出的特点

        :param s:
        :return:
        """
        # d = {
        #     '{': "}",
        #     '[': "]",
        #     '(': ")"
        # }
        d = {
            '}': "{",
            ']': "[",
            ')': "("
        }
        if len(s)%2 != 0 :
            return False

        stack = []
        for st in s:
            if st in d:
                if not stack or stack[-1] != d[st]:
                    return False
                stack.pop()
            else:
                stack.append(st)
        return True if not stack else False



# leetcode submit region end(Prohibit modification and deletion)
so = Solution()
s='(('
print(so.isValid(s))
# print(len(s)/2)