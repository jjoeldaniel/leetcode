# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        res = []

        while q:
            rightSide = None

            # iterate through level
            for i in range(len(q)):
                node = q.popleft()
\
                # set values, if exists
                if node:

                    # we set rightSide equal to each node,
                    # this allows us to catch cases where
                    # the left side is visible due to an
                    # empty right
                    #
                    # the final result is rightSide being
                    # equal to the final node in `q`
                    rightSide = node

                    q.append(node.left)
                    q.append(node.right)

            # append right side node, if exists
            if rightSide: res.append(rightSide.val)
        
        return res
