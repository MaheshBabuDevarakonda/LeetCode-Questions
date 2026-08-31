# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        ne = curr.next
        first=-1
        last=-1

        pos = 1
        lmax=-1
        lmin=float('inf')
        while(ne is not None):
            if (prev.val < curr.val and curr.val > ne.val) or (prev.val > curr.val and curr.val < ne.val):
                if first == -1:
                    first = pos
                else:
                    lmin=min(lmin,pos-last)
                    lmax=pos-first
                last=pos
            pos+=1
            prev=curr
            curr=ne
            ne=ne.next
        if lmin==float('inf'):
            return [-1,-1]
        return [lmin,lmax]



            


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna