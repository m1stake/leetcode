from typing import List


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):

        cn = self
        s = ''
        while cn:
            s += str(cn.val)
            cn = cn.next
            if cn:
                s += '->'
        return s


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        rl = ListNode()

        cn = rl

        while l1 and l2:

            l1_cv = l1.val
            l2_cv = l2.val

            if l1_cv <= l2_cv:
                cn.next = l1
                l1 = l1.next
            else:
                cn.next = l2
                l2 = l2.next

            cn = cn.next

        if l1:
            cn.next = l1
        elif l2:
            cn.next = l2
        else:
            cn.next = None

        return rl.next


def make_listNode(l: List):
    ln = ListNode()
    cn = ln
    for i in l:
        cn.next = ListNode(i)
        cn = cn.next

    return ln.next


print(
    Solution().mergeTwoLists(make_listNode([1,2,3,3]), make_listNode([2,3,4,5]))
)
