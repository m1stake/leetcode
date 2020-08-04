from ListNodeUtils import ListNode, make_listNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if k == 0 or k == 1:
            return head

        cn = head

        fh = ListNode(-1)
        fh.next = head

        pre = fh
        while cn is not None:

            basket = []
            for _ in range(k):
                basket.append(cn)
                cn = cn.next

                if cn is None:
                    break

            if len(basket) == k:

                fbn = basket[0]
                lbn = basket[k - 1]

                fbn.next = lbn.next

                for i in range(1, k):
                    basket[i].next = basket[i - 1]

                pre.next = lbn
                pre = fbn

        return fh.next


print(
    Solution().reverseKGroup(make_listNode([]), 1),
    Solution().reverseKGroup(make_listNode([1]), 0),
    Solution().reverseKGroup(make_listNode([1]), 1),
    Solution().reverseKGroup(make_listNode([1,2]), 1),
    Solution().reverseKGroup(make_listNode([1,2]), 2),
    Solution().reverseKGroup(make_listNode([1,2,3,4]), 2),
    Solution().reverseKGroup(make_listNode([1,2,3,4,5]), 3),

)
