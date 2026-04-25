public class Encryption {
    public String encrypt(String message) {
        int n = message.length();
        char[] result = new char[n];
        
        char[] map = new char[26];
        char nextChar = 'a';

        for (int i = 0; i < n; i++) {
            char currentChar = message.charAt(i);
            int index = currentChar - 'a';

            if (map[index] == 0) {
                map[index] = nextChar;
                nextChar++;
            }

            result[i] = map[index];
        }

        return new String(result);
    }
}
