from collections import deque

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

    def preorder_traversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        results = []

        def preorder(node, results):
            results.append(node.val)
            if node.left is not None:
                preorder(node.left, results)
            if node.right is not None:
                preorder(node.right, results)

        preorder(root, results)

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

    def inorder_traversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def inorder(node, results):
            if node.left:
                inorder(node.left, results)
            results.append(node.val)
            if node.right:
                inorder(node.right, results)

        if not root:
            return []

        results = []
        inorder(root, results)

        return results

    def postorder_traversal_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        results = []
        path = [root]

        while path:
            current = path.pop()
            if current.left is None and current.right is None:
                results.append(current.val)
                continue

            path.append(current)
            if current.right is not None:
                path.append(current.right)
                current.right = None
            if current.left is not None:
                path.append(current.left)
                current.left = None

        return results

    def levelOrder_traversal_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        results = []
        path = [[root]]

        while path:
            temp_out = []
            candidates = []

            current = path.pop()
            for item in current:
                temp_out.append(item.val)
                if item.left is not None:
                    candidates.append(item.left)
                if item.right is not None:
                    candidates.append(item.right)
            if temp_out:
                results.append(temp_out)
            if candidates:
                path.append(candidates)

        return results
