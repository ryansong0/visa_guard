import java.util.*;

public class OlympicCandles {
    public int numberOfNights(int[] candles) {
        int night = 1;
        
        while (true) {
            Arrays.sort(candles);
            
            int num = candles.length;
            if (night > num) {
                return night - 1;
            }
            
            for (int i = 0; i < night; i++) {
                int index = num - 1 - i;
                if (candles[index] == 0) {
                    return night - 1;
                }
                candles[index]--;
            }
            night++;
        }
    }
}