public class HuffmanDecoding {
    public String decode(String archive, String[] dictionary) {
        String result = "";
        String buffer = "";
        
        char[] alphabet = {
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
            'U', 'V', 'W', 'X', 'Y', 'Z'
        };

        for (int i = 0; i < archive.length(); i++) {
            buffer = buffer + archive.charAt(i);
            for (int j = 0; j < dictionary.length; j++) {
                if (buffer.equals(dictionary[j])) {
                    result = result + alphabet[j];
                    buffer = "";
                    break;
                }
            }
        }
        return result;
    }
}