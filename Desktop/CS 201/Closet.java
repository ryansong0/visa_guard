import java.util.*;

public class Closet {
    public String anywhere(String[] list) {
        HashSet<String> uniquewords = new HashSet<>();
        for (String s : list) {
            String[] words = s.split(" ");
            for (String word : words) {
                uniquewords.add(word);
            }
        }
        List<String> sorted = new ArrayList<>(uniquewords);
        Collections.sort(sorted);
        return String.join(" ", sorted);
    }   
}

