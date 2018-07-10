# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorder_traversal(self, root):
        """
        Iterative solution
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        results = []
        path = [root]

        while path:
            current = path.pop()
            results.append(current.val)
            if current.right is not None:
                path.append(current.right)
            if current.left is not None:
                path.append(current.left)

        return results
