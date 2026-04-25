public class PairDown {
    public int[] fold(int[] list) {
        
        int newlength = (list.length + 1) / 2;
        int[] result = new int[newlength];
        for (int i = 0; i < newlength; i++) {
            int first = list[2 * i];
            int second = 0;
            if (2 * i + 1 < list.length) {
                second = list[2 * i + 1];
            }
            result[i] = first + second;
    }
    return result;
}
}
