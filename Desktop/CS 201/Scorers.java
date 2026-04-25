import java.util.*;

public class Scorers {
 public String[] winners(String[] results, int threshold) {
    HashMap<String, Integer> hashmap = new HashMap<>();
    ArrayList<String> order = new ArrayList<>();
    for (String w : results) {
        int colon = w.indexOf(":");
        String playername = w.substring(0, colon);
        String playerscore = w.substring(colon + 1);

        int score = Integer.parseInt(playerscore);

        if (! hashmap.containsKey(playername)) {
            hashmap.put(playername, 0);
            order.add(playername);
        }
        hashmap.put(playername, hashmap.get(playername) + score);
    }

    ArrayList<String> players = new ArrayList<>();
    for (String o : order) {
        int totalval = hashmap.get(o);

        if (totalval > threshold) {
            players.add(o + ":" + totalval);
        }
    }

    return players.toArray(new String[0]);
 }
}
