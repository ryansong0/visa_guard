import java.util.Arrays;
import java.util.List;

public class SandwichBar {
    public int whichOrder(String[] available, String[] orders){
        List<String> bar = Arrays.asList(available);
         for (int i = 0; i < orders.length; i++) {
            String[] newlist = orders[i].split(" ");
            boolean Food = true;
            for (String s : newlist){
                if (!bar.contains(s)) {
                    Food = false;
                    break;
                }
            }
            if (Food){
                return i;
            }
         }
         return -1; 
      }
}
