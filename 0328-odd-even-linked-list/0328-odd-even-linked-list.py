class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Handle 0 or 1 node
        if head is None or head.next is None:
            return head

        values = []

        # Collect odd-position values
        temp = head
        while temp is not None:
            values.append(temp.val)

            if temp.next is None:
                break

            temp = temp.next.next

        # Collect even-position values
        temp = head.next
        while temp is not None:
            values.append(temp.val)

            if temp.next is None:
                break

            temp = temp.next.next

        # Put values back into the linked list
        temp = head
        index = 0

        while temp is not None:
            temp.val = values[index]
            index += 1
            temp = temp.next

        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna