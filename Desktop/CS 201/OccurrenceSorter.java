import java.util.*;

public class OccurrenceSorter {
    public String[] sorter(String[] words, String[] collection) {
        Map<String, Integer> map = new HashMap<String, Integer>();
        for (int i = 0; i < collection.length; i++) {
            String[] splitting = collection[i].split(" ");
            for (int j = 0; j < splitting.length; j++) {
                String val = splitting[j];
                if (map.containsKey(val)) {
                    int containing = map.get(val);
                    map.put(val, containing + 1);
                }
                else {
                    map.put(val, 1);
                }
            }
        }
        String[] result = new String[words.length];
        for (int i = 0; i < words.length; i++) {
            result[i] = words[i];
        }
        for (int i = 0; i < result.length - 1; i++) {
            int indexminimum = i;
            for (int j = i + 1; j < result.length; j++) {
                int firstcount = 0;
                if (map.containsKey(result[j])) {
                    firstcount = map.get(result[j]);
                }
                int countval = 0;
                if (map.containsKey(result[indexminimum])) {
                    countval = map.get(result[indexminimum]);
                }
                if (firstcount < countval) {
                    indexminimum = j;
                }
                else if (firstcount == countval) {
                    if (result[j].compareTo(result[indexminimum]) < 0) {
                        indexminimum = j;
                    }
                }
            }
            String swap = result[indexminimum];
            result[indexminimum] = result[i];
            result[i] = swap;
        }
        return result;
    }
}
