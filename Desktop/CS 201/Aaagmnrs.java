import java.util.*;

public class Aaagmnrs {
    public String[] anagrams(String[] phrases) {
        List<String> result = new ArrayList<>();
        Set<String> hashset = new HashSet<>();

        for (String o : phrases) {
            String normal = normalize(o);

            if (!hashset.contains(normal)) {
                result.add(o);
                hashset.add(normal);
            }
        }
        return result.toArray(new String[0]);
    }

    private String normalize(String s) {
        char[] character = s.toLowerCase().replace(" ", "").toCharArray();
        Arrays.sort(character);
        return new String(character);
    }
}     

