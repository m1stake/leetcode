from typing import List
from ListNodeUtils import ListNode, make_listNode


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        l = []

        cn = head

        while cn:

            l.append(cn)
            if len(l) > n + 1:
                l = l[1:]

            cn = cn.next

        if len(l) == n:
            return l[0].next
        elif n == 1:
            l[0].next = None
            return head
        else:
            l[0].next = l[2]
            return head


print(
    Solution().removeNthFromEnd(make_listNode([1,2,3,4]), 2),
    Solution().removeNthFromEnd(make_listNode([1,2,3,4]), 4),
    Solution().removeNthFromEnd(make_listNode([1]), 1),
    Solution().removeNthFromEnd(make_listNode([1,2]), 1),
)



