public class AddSome {
      public ListNode splice(ListNode list, int size){
        if (list == null || size <= 0) {
            return list;
        }

        ListNode num = list;
        for (int i = 0; i < size - 1; i++) {
            num = num.next;
        }
        ListNode count = num.next;
        ListNode one = null;
        ListNode two = null;
        ListNode pop = list;
          return null;
      }
  }