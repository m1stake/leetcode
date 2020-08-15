from ListNodeUtils import ListNode, make_listNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        low_pre = None
        pre = ListNode(-1)
        pre.next = head
        n = head
        while n is not None:
            print([n.val, pre.val])
            if n.val < x:
                pre.next = n.next

                if low_pre is not None:
                    if low_pre.next is not n:
                        n.next = low_pre.next
                        low_pre.next = n
                    low_pre = n
                else:
                    low_pre = n
                    if low_pre is not head:
                        low_pre.next = head
                        head = low_pre

                n = pre.next
            else:
                pre = n
                n = n.next

        return head


print(
    Solution().partition(make_listNode([1, 1]), 2),
    Solution().partition(make_listNode([3, 3]), 2),
    Solution().partition(make_listNode([5, 2]), 3),
    Solution().partition(make_listNode([3, 3, 4, 5, 1, 2, 3]), 3),
    Solution().partition(make_listNode([1, 4, 3, 2, 5, 2]), 3)
)
