import java.util.*;

public class XList {
    String[] transform(ListNode list) {
        int num = 0;
        ListNode val = list;
        while (val != null) {
            num++;
            val = val.next;
        }
        String[] result = new String[num];
        int index = 0;

        ListNode now = list;
        while (now != null) {
            int count = Math.max(0, now.info);
            char[] character = new char[count];
            for (int i = 0; i < count; i++) {
                character[i] = 'x';
            }
            if (index < result.length) {
                result[index] = new String(character);
            }
            index++;
            now = now.next;
        }
        return result;
    }
}
