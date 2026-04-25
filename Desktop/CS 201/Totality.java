 public class Totality {
     public int sum(int[] a, String stype) {
        int count = 0;
         if (stype.equals("odd")) {
            for (int i = 1; i < a.length; i += 2)
                count = count + a[i];
        }
        if (stype.equals("even")) {
            for (int i = 0; i < a.length; i += 2)
                count = count + a[i];
        }
        if (stype.equals("all")) {
            for (int i = 0; i < a.length; i++)
                count = count + a[i];
         }
         return count;
     }
 }
