import java.util.*;

public class SimpleWordGame {
    public int points(String[] player, String[] dictionary) {
        HashSet<String> p = new HashSet<>();
        HashSet<String> d = new HashSet<>();
        for (String s : player) p.add(s);
        d.addAll(Arrays.asList(dictionary));

        int score = 0;
        for (String s : p) {
            if (d.contains(s)) {
                score += s.length() * s.length();
            }
        }
        return score;
    }
}
