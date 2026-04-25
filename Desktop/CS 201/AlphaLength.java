import java.util.*;

public class AlphaLength {
      public ListNode create (String[] words) {
        if (words == null || words.length == 0) {
            return null;
        }
        Arrays.sort(words);

        ListNode first = null;
        ListNode last = null;
        
        for (int i = 0; i < words.length; i++) {
            if (i > 0 && words[i].equals(words[i - 1])) {
                continue;
            }
            ListNode val = new ListNode(words[i].length());

            if (first == null) {
                first = val;
                last = val;
            }
            else {
                last.next = val;
                last = val;
            }
        }
        return first;
      }
  }