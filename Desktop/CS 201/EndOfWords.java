 import java.util.*;

 public class EndOfWords {
      public String[] filter(String[] words){
        ArrayList<String> newset = new ArrayList<String>();
        Set<Character> hashcheck = new HashSet<>();
        for (String w : words) {
            char one = w.charAt(0);
            if (w.charAt(0) == w.charAt(w.length() - 1)) {
                if (!hashcheck.contains(one)) {
                    newset.add(w);
                    hashcheck.add(one);
                }
            }
        }
        return newset.toArray(new String[0]);
      }
  }