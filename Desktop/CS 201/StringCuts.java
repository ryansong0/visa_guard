import java.util.*;

public class StringCuts {
    public String[] filter(String[] list, int minLength) {
        Set<String> returnSet = new LinkedHashSet<>();

        for (String s : list) {
            if (s.length() >= minLength) {
                returnSet.add(s);
            }
        }

        return returnSet.toArray(new String[0]);
     }
}
