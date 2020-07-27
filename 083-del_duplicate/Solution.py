from ListNodeUtils import ListNode, make_listNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        pre_head = ListNode(-1)
        pre_head.next = head

        pre = pre_head
        cn = head
        cv = None
        while cn:
            if cn.val == cv:
                pre.next = cn.next
            else:
                cv = cn.val
                pre = cn

            cn = cn.next

        return pre_head.next


print(
    Solution().deleteDuplicates(make_listNode([])),
    Solution().deleteDuplicates(make_listNode([1])),
    Solution().deleteDuplicates(make_listNode([1,1])),
    Solution().deleteDuplicates(make_listNode([1,1,2,3,3,4])),
    Solution().deleteDuplicates(make_listNode([1,1,2,3,3,4,4])),

)
