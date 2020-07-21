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


def make_listNode(l: List):
    ln = ListNode()
    cn = ln
    for i in l:
        cn.next = ListNode(i)
        cn = cn.next

    return ln.next