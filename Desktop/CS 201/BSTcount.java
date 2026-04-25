import java.util.*;

public class BSTcount {
    public long howMany(int[] values) {
        int num = values.length;
        if (num <= 1) {
            return 1;
        }

        long[] unique = new long[num + 1];
        
        unique[0] = 1; 
        unique[1] = 1; 

        for (int i = 2; i <= num; i++) {
            for (int j = 1; j <= i; j++) {
                unique[i] += unique[j - 1] * unique[i - j];
            }
        }
        return unique[num];
    }
}