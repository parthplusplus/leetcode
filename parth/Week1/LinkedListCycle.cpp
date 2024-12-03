/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr)
        {
            return false;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast != nullptr)
        {
            slow = slow->next;
            fast = fast->next!=nullptr ? fast->next->next : nullptr;
            if (slow == fast)
            {
                return true;
            }
        }
        return false;
    }
};