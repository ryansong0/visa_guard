import java.util.*;

public class VowelHeavy {
    public int countHeavy(String[] words) {
        int vowelwords = 0;
        for (int i = 0; i < words.length; i++) {
            int vowels = 0;
            int consonants = 0;
            for (int j = 0; j < words[i].length(); j++) {
                char character = words[i].charAt(j);
                if (character == 'a' || character == 'e' || character == 'i' || character == 'o' || character == 'u') {
                    vowels++;
                }
                else {
                    consonants++;
                }
            }
            if (vowels > consonants) {
                vowelwords++;
            }
        }
        return vowelwords;
        }
    }
