public class List2Long {
      public long convert(ListNode list) {
        long val = 0;
        ListNode num = list;

        while (num != null) {
            val = val * 10 + num.info;

            num = num.next;
        }
         return val; 
      }
  }
