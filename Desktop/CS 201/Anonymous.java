import java.util.*;

public class Anonymous {
    public int howMany(String[] headlines, String[] messages) {
        String headlineStrings = String.join(" ", headlines);
        Map<Character,Integer> headlineMap = helper(headlineStrings);

        int count = 0;
        for (String s : messages) {
            Map<Character,Integer> map = helper(s);

            if (canMake(map, headlineMap)) {
                count++;
            }
        }
        return count;
    } 

    private boolean canMake(Map<Character,Integer> map, Map<Character,Integer> headlineMap) {
        for (char ch : map.keySet()) {
            int mcount = map.get(ch);
            int hcount = headlineMap.getOrDefault(ch,0);
            if (mcount > hcount) {
                return false;
            }
        }
        return true;
    }

    private Map<Character,Integer> helper(String s) {
        Map<Character,Integer> map = new HashMap<>();
        for (char ch : s.toLowerCase().toCharArray()) {
            if (ch == ' ') continue;
            int count = map.getOrDefault(ch, 0);
            map.put(ch, count+1);
        }
        return map;
    }
}
