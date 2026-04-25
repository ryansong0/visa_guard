import java.util.*;

public class SortedFreqs {
      public int[] freqs(String[] data) {
        if (data == null || data.length == 0) {
            return new int[0];
        }

        TreeMap<String, Integer> map = new TreeMap<>();
        for (String d : data) {
            map.put(d, map.getOrDefault(d, 0) + 1);
        }
        int[] result = new int[map.size()];
        int index = 0;

        for (int count : map.values()) {
            result[index] = count;
            index++;
        }
        return result;
      }
}
