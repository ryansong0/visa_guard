import java.util.*;

public class LevelCount {
    public int count(TreeNode t, int level) {
        if (t == null) {
            return 0;
        }
        if (level == 0) {
            return 1;
        }
        int leftco = count(t.left, level - 1);
        int rightco = count(t.right, level - 1);

        return leftco + rightco;
    }
}
