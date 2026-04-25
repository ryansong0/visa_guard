public class ListSum {
    public int sum(ListNode list, int thresh) {
        int sum = 0;
        ListNode now = list;

        while (now != null) {
            if (now.info > thresh){
                sum += now.info;
            }
            now = now.next;
        }
	  return sum;
      }
}
