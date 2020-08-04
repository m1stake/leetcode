from typing import List
from ListNodeUtils import ListNode, make_listNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head:
            return head

        if head.next:
            h = head.next
        else:
            h = head

        cn1 = head
        cn2 = head.next
        pre = None

        while cn1 is not None and cn2 is not None:

            if pre:
                pre.next = cn2

            cn1.next = cn2.next
            cn2.next = cn1
            pre = cn1

            cn1 = pre.next
            if cn1 is not None:
                cn2 = cn1.next
            else:
                break

        return h


print(
    Solution().swapPairs(make_listNode([1])),
    Solution().swapPairs(make_listNode([1, 2])),
    Solution().swapPairs(make_listNode([1, 2, 3])),
    Solution().swapPairs(make_listNode([1,2,3,4]))

)