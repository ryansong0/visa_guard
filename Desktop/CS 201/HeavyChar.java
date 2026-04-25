import java.util.*;

public class HeavyChar {
    public String[] weight(String[] words, String letter, int minChars){
        ArrayList<String> morewords = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            int sum = 0;
            for (int j = 0; j < words[i].length(); j++) {
                if (words[i].substring(j, j + 1).equals(letter)) {
                    sum++;
                }
            }
            if (sum > minChars) {
                    morewords.add(words[i]);
                }
        }

        return morewords.toArray(new String[0]);
      }
  }
