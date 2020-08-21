r"""
110. 二叉树的后序遍历
url: https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

题解：[模仿递归](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/mo-fang-di-gui-zhi-bian-yi-xing-by-sonp/)

给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """递归"""
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal_(self, root: TreeNode) -> List[int]:
        """迭代"""
        if not root:
            return []
        res, stack = [], []
        cur = root
        r = None
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack[-1]
                if cur.right is None or cur.right == r:
                    res.append(cur.val)
                    r = cur
                    stack.pop()
                    cur = None
                else:
                    cur = cur.right
        return res