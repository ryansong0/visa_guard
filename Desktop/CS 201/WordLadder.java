import java.util.*;

public class WordLadder {
    public String ladderExists(String[] words, String from, String to) {
        Set<String> every = new HashSet<>(Arrays.asList(words));
        every.add(from);
        every.add(to);

        Map<String, Integer> fromdis = bfs(from, every);
        Map<String, Integer> todis = bfs(to, every);

        int shortdis = fromdis.getOrDefault(to, Integer.MAX_VALUE);
                if (shortdis == Integer.MAX_VALUE || shortdis <= 1) {
            return "none";
        } 

        for (String val : words) {
            if (fromdis.containsKey(val) && todis.containsKey(val)) {
                if (fromdis.get(val) + todis.get(val) == shortdis) {
                    return "ladder";
                }
            }
        }

        return "none";
    }

    private Map<String, Integer> bfs(String start, Set<String> dict) {
        Map<String, Integer> dist = new HashMap<>();
        Queue<String> queue = new LinkedList<>();
        
        queue.add(start);
        dist.put(start, 0);
        
        while (!queue.isEmpty()) {
            String curr = queue.poll();
            for (String neighbor : dict) {
                if (!dist.containsKey(neighbor) && one(curr, neighbor)) {
                    dist.put(neighbor, dist.get(curr) + 1);
                    queue.add(neighbor);
                }
            }
        }
        return dist;
    }

    private boolean one(String a, String b) {
        if (a.length() != b.length()) {
            return false;
        }
        int diff = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                diff++;
            }   
            if (diff > 1) {
                return false;
            }
        }
        return diff == 1;
    }
}