import java.util.*;

public class MedalTable {
    public String[] generate(String[] results) {
        List<String> countries = new ArrayList<>();
        for (String o : results) {
            for (String r : o.split(" ")) {
                if (!countries.contains(r)) {
                    countries.add(r);
                }
            }
        }
        int n = countries.size();
        String[] vals = new String[n];
        int[] a = new int[n];
        int[] b = new int[n];
        int[] c = new int[n];

        for (int s = 0; s < n; s++) {
            vals[s] = countries.get(s);
            for (String o : results) {
                String[] things = o.split(" ");
                if (things[0].equals(vals[s])) {
                    a[s]++;
                }
                if (things[1].equals(vals[s])) {
                    b[s]++;
                }
                if (things[2].equals(vals[s])) {
                    c[s]++;
                }
            }
        }
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                boolean pop = false;

                if (a[j] > a[i]) {
                    pop = true;
                }
                else if (a[j] == a[i]) {
                    if (b[j] > b[i]) {
                        pop = true;
                    }
                    else if (b[j] == b[i]) {
                        if (c[j] > c[i]) {
                            pop = true;
                        }
                        else if (c[j] == c[i]) {
                            if (vals[j].compareTo(vals[i]) < 0) {
                                pop = true;
                            }
                        }
                    }
                }
                if (pop) {
                    int gold = a[i];
                    a[i] = a[j];
                    a[j] = gold;

                    int silver = b[i];
                    b[i] = b[j];
                    b[j] = silver;

                    int bronze = c[i];
                    c[i] = c[j];
                    c[j] = bronze;

                    String name = vals[i];
                    vals[i] = vals[j];
                    vals[j] = name;
                    }
                }
            }
        String[] finalnum = new String[n];
        for (int k = 0; k < n; k++) {
            finalnum[k] = vals[k] + " " + a[k] + " " + b[k] + " " + c[k];
        }
        return finalnum;
        }
    }
