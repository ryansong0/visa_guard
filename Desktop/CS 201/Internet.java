import java.util.*;

public class Internet {
    public int articulationPoints(String[] routers) {
        int num = routers.length;
        int total = 0;
        for (int i = 0; i < num; i++) {
            boolean[] verify = new boolean[num];
            verify[i] = true;
            int components = 0;
            for (int j = 0; j < num; j++) {
                if (!verify[j]) {
                    components++;
                    Queue<Integer> val = new LinkedList<>();
                    val.add(j); 
                    verify[j] = true;
                    while (!val.isEmpty()) {
                        for (String s : routers[val.poll()].split(" ")) {
                            int check = Integer.parseInt(s);
                            if (!verify[check]) { 
                                verify[check] = true; 
                                val.add(check); 
                            }
                        }
                    }
                }
            }
            if (components > 1) {
                total++;
            }
        }
        return total;
    }
}