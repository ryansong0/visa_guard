public class ListLastFirst {
    public ListNode move(ListNode list) {
        if (list == null || list.next == null) {
            return list;
    }
    ListNode current = list;
    while (current.next.next != null) {
        current = current.next;
    }
    ListNode lastnode = current.next;
    current.next = null;
    lastnode.next = list;
    return lastnode;
        }
    }
