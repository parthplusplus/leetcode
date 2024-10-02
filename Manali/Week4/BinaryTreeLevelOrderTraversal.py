# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        if not root: return []
        ans = []
        queue.append(root)
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                level.append(node.val)
            if level: ans.append(level)
        return ans
        
# TC: O(n)
# SC: O(w), where w is max width of tree