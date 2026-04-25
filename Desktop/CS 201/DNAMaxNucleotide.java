public class DNAMaxNucleotide{
    public String max(String[] strands, String nuc) {
        String ret = "";
        int maxCount = 0;
        char want = nuc.charAt(0);

        for (int i = 0; i < strands.length; i++) {
            String currentStrand = strands[i];
            int currentCount = 0;
            
            for (char c : currentStrand.toCharArray()) {
                if (c == want) {
                    currentCount++;
                }
            }

            if (currentCount > maxCount) {
                maxCount = currentCount;
                ret = currentStrand;
            } else if (currentCount == maxCount && currentCount > 0) {
                if (currentStrand.length() > ret.length()) {
                    ret = currentStrand;
                }
            }
        }
        return ret;
    }
}

