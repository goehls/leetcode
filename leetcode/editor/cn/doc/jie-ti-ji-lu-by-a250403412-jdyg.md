解法：和[7. 整数反转](/problems/reverse-integer/)思路一样
C++和C#在用不到数组时语法一样啊。。。
C++也就抄抄[@LeetCode-Solution](/u/leetcode-solution/)。。。
```c++ []
//执行用时: 8 ms；内存消耗: 5.8 MB
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        int revertedNumber = 0;
        while (x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }
        return x == revertedNumber || x == revertedNumber / 10;
    }
};
```
```C# []
//执行用时: 72 ms；内存消耗: 16 MB
public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        int revertedNumber = 0;
        while (x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }
        return x == revertedNumber || x == revertedNumber / 10;
    }
}
```
```python3 []
#执行用时: 84 ms；内存消耗: 15 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            s=list(str(x))
            s_c=s.copy()
            s_c.reverse()
            if s==s_c:
                return True
            else:
                return False
```
