public class TxMsg {
    public String getMessage(String original) {
        String[] words = original.split(" ");
        for (int k = 0; k < words.length; k++) {
            words[k] = convert(words[k]);
        }
        return String.join(" ", words);
    }

    private boolean allVowels(String s) {
        for (char ch : s.toCharArray()) {
            if (! isVowel(ch)) {
                return false;
            }
        }
        return true;
    }

    private boolean isVowel(char ch) {
        return "aeiou".indexOf(ch) >=0;
    }

    private String convert(String str) {
        if (allVowels(str)) {
            return str;
        }
        String ret = "";
        if (! isVowel(str.charAt(0))) {
                ret += str.charAt(0);
        }
        for (int k = 1; k < str.length(); k++) {
            char now = str.charAt(k);
            char before = str.charAt(k-1);
            if (! isVowel(now) && isVowel(before)) {
                ret += now;
            }
        }
        return ret;
    }


    public static void main(String[] args) {
        System.out.println("text message hello");
    }
        
}
