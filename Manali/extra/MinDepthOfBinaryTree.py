class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = collections.deque()
        queue.append(root)
        ct = 1
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if not node.left and not node.right: return ct
            ct+=1
        return ct

TC: O(n)
SC: O(w)