  carry = 0
        root = l3 = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            carry,val3 = divmod(val1+val2+carry,10)
            l3.next = ListNode(val3)
            l3 = l3.next
        return root.next
            
