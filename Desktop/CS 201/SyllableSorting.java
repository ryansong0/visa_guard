import java.util.*;

public class SyllableSorting {
    public String[] sortWords(String[] words) {
        int n = words.length;

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                String word1 = words[j];
                String word2 = words[j + 1];

                ArrayList<String> syllabus = new ArrayList<>();
                int index = 0;
                while (index < word1.length()) {
                    int start = index;
                    while (index < word1.length() && "aeiou".indexOf(word1.charAt(index)) == -1) {
                        index++;
                    }
                    while (index < word1.length() && "aeiou".indexOf(word1.charAt(index)) != -1) {
                        index++;
                    }
                    syllabus.add(word1.substring(start, index));
                }
                ArrayList<String> secondsyl = new ArrayList<>();
                int count = 0;
                while (count < word2.length()) {
                    int begin = count;
                    while (count < word2.length() && "aeiou".indexOf(word2.charAt(count)) == -1) {
                        count++;
                    }
                    while (count < word2.length() && "aeiou".indexOf(word2.charAt(count)) != -1) {
                        count++;
                    }
                    secondsyl.add(word2.substring(begin, count));
                }
                ArrayList<String> sortone = new ArrayList<>(syllabus);
                ArrayList<String> sortsecond = new ArrayList<>(secondsyl);
                Collections.sort(sortone);
                Collections.sort(sortsecond);

                int comparison = 0;
                int w = 0;
                int minimum = Math.min(sortone.size(), sortsecond.size());
                while (w < minimum && comparison == 0) {
                    comparison = sortone.get(w).compareTo(sortsecond.get(w));
                    w++;
                }
            
                if (comparison == 0) {
                    comparison = sortone.size() - sortsecond.size();
                }
                if (comparison > 0) {
                    String temp = words[j];
                    words[j] = words[j + 1];
                    words[j + 1] = temp;
                }
            }
        }
        return words;
    }
}
