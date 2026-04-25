public class SoccerLeagues {
    public int[] points(String[] matches) {
        int numTeams = matches.length;
        int[] totalPoints = new int[numTeams];

        for (int i = 0; i < numTeams; i++) {
            for (int j = 0; j < numTeams; j++) {
                char result = matches[i].charAt(j);

                if (result == 'W') {
                    totalPoints[i] += 3;
                } else if (result == 'D') {
                    totalPoints[i] += 1;
                    totalPoints[j] += 1;
                } else if (result == 'L') {
                    totalPoints[j] += 3;
                }
            }
        }
        return totalPoints;
    }
}
