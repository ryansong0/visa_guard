import java.util.*;

public class LengthSort {
    public String[] rearrange(String[] values) {
        if (values == null || values.length == 0) {
            return values;
        }
        
        Arrays.sort(values, new Comparator<String>() {
            @Override
            public int compare(String first, String second) {
                if (first.length() != second.length()) {
                    return Integer.compare(first.length(), second.length());
                }
                return first.compareTo(second);
            }
        });
        return values;
    }
}
