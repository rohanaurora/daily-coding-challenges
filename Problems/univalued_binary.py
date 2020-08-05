class Solution(object):
    def isUnivalTree(self, root: TreeNode) -> bool:
        # iteration
        #O(n)time O(logn)space
        node = root
        stack =[]
        stack.append(node)
        prev = root.val
        while stack:
            node = stack.pop()
            if node.val != prev:
                return False
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return True