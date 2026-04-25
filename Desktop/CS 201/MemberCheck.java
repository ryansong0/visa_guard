import java.util.*;

public class MemberCheck {
    public String[] whosDishonest(String[] club1, String[] club2, String[] club3) {
        Set<String> s1 = new HashSet<>(Arrays.asList(club1));
        Set<String> s2 = new HashSet<>(Arrays.asList(club2));
        Set<String> s3 = new HashSet<>(Arrays.asList(club3));

        Set<String> dishonestSet = new HashSet<>();

        for (String name : s1) {
            if (s2.contains(name) || s3.contains(name)) {
                dishonestSet.add(name);
            }
        }

        for (String name : s2) {
            if (s3.contains(name)) {
                dishonestSet.add(name);
            }
        }

        String[] result = dishonestSet.toArray(new String[0]);
        Arrays.sort(result);

        return result;
    }
}