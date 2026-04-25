import java.util.*;

public class Ograph {
    public int[] components(String[] data) {
        int num = data.length;
        boolean[] visit = new boolean[num];
        List<Integer> sizes = new ArrayList<>();

        for (int i = 0; i < num; i++) {
            if (!visit[i]) {
                sizes.add(count(i, data, visit));
            }
        }

        int[] result = new int[sizes.size()];
        for (int i = 0; i < sizes.size(); i++) {
            result[i] = sizes.get(i);
        }
        Arrays.sort(result);
        return result;
    }

    private int count(int node, String[] data, boolean[] visit) {
        visit[node] = true;
        int val = 1;

        String[] neighbors = data[node].split(" ");
        for (String s : neighbors) {
            if (s.isEmpty()) {
                continue;
            } 
            int neighbor = Integer.parseInt(s);
            if (!visit[neighbor]) {
                val += count(neighbor, data, visit);
            }
        }
        return val;
    }
}