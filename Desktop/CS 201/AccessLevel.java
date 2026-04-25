public class AccessLevel {
    public String canAccess(int[] rights, int minPermission) {
        String ret = "";
        for(int val : rights) {
            if (val >= minPermission) {
                ret += "A";
            }
            else {
                ret += "D";
            }
        }
       return ret;
    }
}
