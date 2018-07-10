# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorder_traversal_iterative(self, root):
        """
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

    def inorder_traversal_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        results = []
        path = [root]
        current = root

        while current.left is not None:
            current = current.left
            path.append(current)

        while path:
            current = path.pop()
            results.append(current.val)

            if current.right is not None:
                current = current.right
                path.append(current)

                while current.left is not None:
                    current = current.left
                    path.append(current)

        return results
