public class ListParity {
      public int count (ListNode list){
        int sum = 0;
        int pop = 0;
        ListNode one = list;


        while (one != null) {
            if (pop % 2 == 0) {
                sum += one.info;
            }
            pop++;
            one = one.next;
        }
        return sum;
      }
  }