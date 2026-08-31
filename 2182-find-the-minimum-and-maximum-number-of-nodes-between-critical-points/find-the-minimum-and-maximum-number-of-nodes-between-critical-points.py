# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head 
        cur = head.next
        idx = 1

        firstcritical = -1
        lastcritical = -1
        mindist = float('inf')

        while cur.next:
            nxt = cur.next
            if (cur.val > prev.val and cur.val > nxt.val) or (cur.val < prev.val and cur.val < nxt.val):
                if lastcritical == -1:
                    firstcritical = idx
                else:
                    mindist = min(mindist, idx - lastcritical)
                
                lastcritical = idx
            prev = cur
            cur = nxt
            idx += 1

        if firstcritical == -1 or firstcritical == lastcritical:
            return [-1,-1]
        maxdist = lastcritical - firstcritical

        return [mindist,maxdist]