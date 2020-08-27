r"""
104. 朋友圈
url: https://leetcode-cn.com/problems/friend-circles/

班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

 

示例 1：

输入：
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出：2 
解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回 2 。
示例 2：

输入：
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出：1
解释：已知学生 0 和学生 1 互为朋友，学生 1 和学生 2 互为朋友，所以学生 0 和学生 2 也是朋友，所以他们三个在一个朋友圈，返回 1 。
 

提示：

1 <= N <= 200
M[i][i] == 1
M[i][j] == M[j][i]
"""
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N, visited, res = len(M), set(), 0
        for i in range(N):
            if i in visited:
                # 该学生已拜访过
                continue
            queue = [i] # 当前拜访的学生入队
            while queue:
                p = queue.pop(0) # 学生按先后顺序出队
                if p not in visited: # 如果没拜访过这个学生
                    visited.add(p) # 添加到已拜访
                    queue += [k for k, num in enumerate(M[p]) if num and k not in visited] # 拜访的时候做点事情, 1. 看看有没有没拜访过的学生是当前正在拜访学生的朋友, 有的话入队
            res += 1 # 收集到一个朋友圈
        return res

