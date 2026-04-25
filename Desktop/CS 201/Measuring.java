import java.util.*;

public class Measuring {
      public int[] calculate(String[] data) {
          ArrayList<Integer> newarr = new ArrayList<>();
          Set<String> newhash = new HashSet<>();
          for (String w : data) {
            if (! newhash.contains(w)) {
                newarr.add(w.length());
                newhash.add(w);
            }
            else {
                newarr.add(0);
            }
          }

          int[] result = new int[newarr.size()];
          for (int i = 0; i < newarr.size(); i++) {
            result[i] = newarr.get(i);
          }
          return result;
      }
  }