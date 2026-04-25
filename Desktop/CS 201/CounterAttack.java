import java.util.*;

public class CounterAttack {
    public int[] analyze(String str, String[] words) {
         int ret[] = new int[words.length];

         String[] temp = str.split(" ");
         List<String> list = Arrays.asList(temp);

         for (int k = 0; k < words.length; k++) {
            ret[k] = Collections.frequency(list, words[k]);
         }
         return ret;
     }
}
