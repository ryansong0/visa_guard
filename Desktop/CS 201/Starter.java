import java.util.ArrayList;

public class Starter {
     public int begins(String[] words, String first) {
        ArrayList<String> newlist = new ArrayList<>();
        int count = 0;
         for (int i = 0; i < words.length; i++){
            if (words[i].startsWith(first) && !newlist.contains(words[i])) {
                newlist.add(words[i]);
                count++;
            }
         }
         return count;
     }
 }
