public class MergeLists {
      public ListNode weave (ListNode a, ListNode b) {
        if (a == null) {
            return b;
        }
        if (b == null) {
            return a;
        }
        ListNode num1 = a;
        ListNode num2 = b;

        while (num1 != null && num2 != null) {
            ListNode nodelist1 = num1.next;
            ListNode nodelist2 = num2.next;

            num1.next = num2;

            if (nodelist1 != null) {
                num2.next = nodelist1;
            }
            num1 = nodelist1;
            num2 = nodelist2;
        }
        return a;
      }
  }