import java.util.*;

public class SortByFreqs {
    public String[] sort(String[] data) {
        if (data == null || data.length == 0) {
            return new String[0];
        }

        Map<String, Integer> frequency = new HashMap<>();
        for (String d : data) {
            frequency.put(d, frequency.getOrDefault(d, 0) + 1);
        }

        List<String> unique = new ArrayList<>(frequency.keySet());
        Collections.sort(unique, new Comparator<String>() {
            @Override
            public int compare(String first, String second) {
                int val1 = frequency.get(first);
                int val2 = frequency.get(second);

                if (val1 != val2) {
                    return val2 - val1;
                }

                return first.compareTo(second);
            }
        });
        String[] result = new String[unique.size()];
        return unique.toArray(new String[0]);
    }
}
