# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([root])
        res = []

        while q:
            t = []

            # iterate through level
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    t.append(node.val)

                    q.append(node.left)
                    q.append(node.right)

            # append all values in level
            if t:
                res.append(t)

        return res
