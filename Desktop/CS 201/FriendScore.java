import java.util.*;

public class FriendScore {
    public int highestScore(String[] friends) {
        int n = friends.length;
        int max = 0;

        for (int i = 0; i < n; i++) {
            int current = 0;

            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (friends[i].charAt(j) == 'Y') {
                    current++;
                } 
                else {
                    for (int k = 0; k < n; k++) {
                        if (friends[i].charAt(k) == 'Y' && friends[k].charAt(j) == 'Y') {
                            current++;
                            break;
                        }
                    }
                }
            }
            if (current > max) {
                max = current;
            }
        }
        return max;
    }
}