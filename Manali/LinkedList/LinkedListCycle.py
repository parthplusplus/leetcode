# "Floyd's Cycle-Finding Algorithm" or "Tortoise and Hare Algorithm".
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast: return True
        return False
    
TC: O(n)
SC: O(1)
        