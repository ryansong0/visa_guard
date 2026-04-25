public class RemoveMin {
    public ListNode remove(ListNode list) {
        if (list == null) {
            return null;
    }
    int minimum = list.info;
    ListNode val = list;
    while (val != null) {
        if (val.info < minimum) {
            minimum = val.info;
        }
        val = val.next;
    }
    if (list.info == minimum) {
        return list.next;
    }
    ListNode current = list;
    boolean check = false;
    
    while (current.next != null && !check) {
        if (current.next.info == minimum) {
            current.next = current.next.next;
            check = true; 
        } 
        else {
            current = current.next;
            }
        }
    return list;
    }
}
