# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：l1 = [], l2 = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  两个链表的节点数目范围是 [0, 50] 
#  -100 <= Node.val <= 100 
#  l1 和 l2 均按 非递减顺序 排列 
#  
#  Related Topics 递归 链表 
#  👍 1619 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        递归法：需要熟练链表
        时间复杂度：O(n+m)
        空间复杂度：O(n+m)
        //(1,1):代表第一次进入递归函数，并且从第一个口进入，并且记录进入前链表的状态
        merge(1,1): 1->4->5->null, 1->2->3->6->null
            merge(2,2): 4->5->null, 1->2->3->6->null
                merge(3,2): 4->5->null, 2->3->6->null
                    merge(4,2): 4->5->null, 3->6->null
                        merge(5,1): 4->5->null, 6->null
                            merge(6,1): 5->null, 6->null
                                merge(7): null, 6->null
                                return l2
                            l1.next --- 5->6->null, return l1
                        l1.next --- 4->5->6->null, return l1
                    l2.next --- 3->4->5->6->null, return l2
                l2.next --- 2->3->4->5->6->null, return l2
            l2.next --- 1->2->3->4->5->6->null, return l2
        l1.next --- 1->1->2->3->4->5->6->null, return l1


        :param l1:
        :param l2:
        :return:
        """
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 and l2:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next,l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        迭代法：
        时间复杂度：O(n+m)
        空间复杂度：O(1)
        :param l1:
        :param l2:
        :return:
        """
        prehead = ListNode(-1)
        pre = prehead
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next =  l1 if l1 else l2
        return prehead.next
    def f(self,x):
        if x >=1:
            return x + self.f(x-1)
        else:
            return 0

    def listToListNode(self,l: list)->ListNode:

        head = ListNode(-1)
        e = 0
        while e < len(l):
            print(l[e])
            head.next = ListNode(l[e])
            head = head.next
            e += 1
        return head

# leetcode submit region end(Prohibit modification and deletion)


s = Solution()
l1 = [1,2,6]
l2 = [1,3,4]

l1 = s.listToListNode(l1)
l2 = s.listToListNode(l2)
# print(l1.val)
# print()
# ln = s.mergeTwoLists(l1, l2)
# print(ln.val)
# print(ln.next.val)
# print(ln.next.next.val)
# print(type(ln))
# for i in range(6):
#     print(ln.val)
    # ln=ln.next
print(s.f(5))
