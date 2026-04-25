public class TrueSpace {
    public long calculateSpace(int[] sizes, int clusterSize) {
        long total = 0;

        for (int size : sizes) {
            if (size > 0) {
                long num = size / clusterSize;

                if (size % clusterSize != 0) {
                    num++;
                }

                total += num * clusterSize;
            }
        }
        return total;
      }
}
