import java.util.*;

public class BigWord {
    public String most(String[] sentences) {
        Map<String, Integer> counts = new HashMap<>();

        for (String s : sentences) {
            String[] words = s.toLowerCase().split(" ");
            for (String y : words) {
                if (y.length() > 0) {
                    counts.put(y, counts.getOrDefault(y, 0) + 1);
                }
            }
        }
        String greatest = "";
        int highestval = -1;
        
        for (String word : counts.keySet()) {
            int currentval = counts.get(word);
            if (currentval > highestval) {
                highestval = currentval;
                greatest = word;
            }
        }
        return greatest;
      }
}
