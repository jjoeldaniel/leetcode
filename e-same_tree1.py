# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a = deque([p])
        b = deque([q])

        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False

        while a:
            for i in range(len(a)):
                node1 = a.popleft()
                node2 = b.popleft()

                if node1.left:
                    left1 = node1.left
                    left2 = node2.left

                    if left1 is None and left2 is not None:
                        return False
                    if left1 is not None and left2 is None:
                        return False

                    if left1.val != left2.val:
                        return False
                    a.append(node1.left)
                    b.append(node2.left)

                if node1.right:
                    right1 = node1.right
                    right2 = node2.right

                    if right1 is None and right2 is not None:
                        return False
                    if right1 is not None and right2 is None:
                        return False

                    if right1.val != right2.val:
                        return False
                    a.append(node1.right)
                    b.append(node2.right)

        return True
