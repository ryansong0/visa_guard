import java.util.*;

public class ListStretch {
    public ListNode stretch(ListNode list, int amount){
        if (list == null || amount <= 0) {
            return null;
        }
        if (amount == 1) {
            return list;
        }
        ListNode current = list;

        while (current != null) {
            for (int i = 0; i < amount - 1; i++) {
                ListNode nextval = new ListNode(current.info, current.next);
                current.next = nextval;
                current = current.next;
            }
            current = current.next;
        }
        return list;
    }
}
