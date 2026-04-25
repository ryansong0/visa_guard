import java.util.*;

public class TreeTighten {
    public TreeNode tighten(TreeNode t) {
        if (t == null) {
            return null;
        }

        t.left = tighten(t.left);
        t.right = tighten(t.right);

        if (t.left == null && t.right != null) {
            return t.right;
        } else if (t.left != null && t.right == null) {
            return t.left;
        }
        return t;
    }
}