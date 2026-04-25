public class ListsEqual {
      public int equal (ListNode a1, ListNode a2) {
        ListNode value = a1;
        ListNode num = a2;

        while (value != null && num != null) {
            if (value.info != num.info) {
                return 0;
            }

            value = value.next;
            num = num.next;
        }
        if (value == null && num == null) {
            return 1;
        }
        else {
            return 0;
        }
    }
  }