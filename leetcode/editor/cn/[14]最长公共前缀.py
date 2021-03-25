# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#  
# 
#  示例 2： 
# 
#  
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] 仅由小写英文字母组成 
#  
#  Related Topics 字符串 
#  👍 1516 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def longestCommonPrefix_1(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        str1 = strs[0]
        pre = ""
        for i in range(1,len(str1)+1):
            for j in range(1,len(strs)):
                if str1[0:i] != strs[j][0:i]:
                    pre = str1[0:i-1]
                    return pre
                pre = str1[0:i]
        return pre

    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                pre += tmp[0]
            else:
                return pre
        return pre


# leetcode submit region end(Prohibit modification and deletion)

s= Solution()
# strs = ["dog","dog","dog"]
strs = ["flower", "flow", "flight"]
print(s.longestCommonPrefix(strs))