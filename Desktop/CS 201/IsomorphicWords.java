public class IsomorphicWords {
    public int countPairs(String[] words) {
        int count = 0;
        int n = words.length;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isIsomorphic(words[i], words[j])) {
                    count++;
                }
            }
        }
        return count;
    }

    private boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] positionr = new int[256];
        int[] positions = new int[256];

        for (int i = 0; i < s.length(); i++) {
            int charr = s.charAt(i);
            int chars = t.charAt(i);

            if (positionr[charr] != positions[chars]) {
                return false;
            }

            positionr[charr] = i + 1;
            positions[chars] = i + 1;
        }
        return true;
    }
}