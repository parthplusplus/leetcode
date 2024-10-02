class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = collections.deque()
        queue.append(root)
        ans = []
        while queue:
            sum = 0
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                sum+=node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(sum/n)
        return ans
    
TC:O(n)
SC:O(w)