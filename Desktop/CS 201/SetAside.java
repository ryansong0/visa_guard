import java.util.*;

public class SetAside {
    public String common(String[] list) {
        if (list == null || list.length == 0) {
            return "";
        }
        String[] initial = list[0].split(" ");
        HashSet<String> common = new HashSet<>(Arrays.asList(initial));

        for (int i = 1; i < list.length; i++) {
            String[] currentword = list[i].split(" ");
            HashSet<String> theset = new HashSet<>(Arrays.asList(currentword));
            common.retainAll(theset);
        }

        List<String> result = new ArrayList<>(common);
        Collections.sort(result);

        return String.join(" ", result);
    }
}
