import java.util.*;

public class LongestRun {
    public String[] findRuns(String[] words) {
        ArrayList<String> run = new ArrayList<>();
       
        for (int i = 0; i < words.length; i++) {
            int maxlength = 1;
            int currentlength = 1;
            char maxchar = (words[i]).charAt(0);
            for (int j = 1; j < words[i].length(); j++) {
                if (words[i].charAt(j) == words[i].charAt(j - 1)) {
                    currentlength++;
                }
                else {
                    currentlength = 1;
                }

                if (currentlength > maxlength) {
                    maxlength = currentlength;
                    maxchar = words[i].charAt(j);
                }
            }
            run.add(maxchar + ":" + maxlength);
        }
        return run.toArray(new String[0]);
    }
}
