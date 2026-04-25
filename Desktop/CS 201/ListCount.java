public class ListCount {
    public int count (ListNode list) {
        int count = 0;
        ListNode now = list;

        while (now != null) {
            count++;
            now = now.next;
        }
	  return count;
      }
}
