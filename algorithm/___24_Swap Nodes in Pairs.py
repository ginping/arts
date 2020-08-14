r"""
24. 两两交换链表中的节点
url: https://leetcode-cn.com/problems/swap-nodes-in-pairs/

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
"""

# Definition for a binary tree node.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        递归两两交换，递归终止条件只剩一个节点或者不剩节点，每一步交换两个节点即可。
        先拿到head.next，然后将交换好的head.next.next接到head上，再把head接到head.next上即可。
        """
        if not head or not head.next:
            return head
        n: ListNode = head.next
        head.next = self.swapPairs(n.next)
        n.next = head
        return n
