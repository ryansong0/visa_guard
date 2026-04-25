import java.util.*;

public class TreeCountIf {
    public int count(TreeNode tree, int thresh) {
        if (tree == null) {
            return 0;
        }
        int val = 0;
        if (tree.info > thresh) {
            val = 1;
        }
        return val + count(tree.left, thresh) + count(tree.right, thresh);
    }
}
