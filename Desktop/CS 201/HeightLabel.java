import java.util.*;

public class HeightLabel {
    public TreeNode rewire(TreeNode t) {
        if (t == null) {
            return null;
        }
        int current = height(t);
        TreeNode newnode = new TreeNode(
            current, 
            rewire(t.left), 
            rewire(t.right)
        );
        return newnode;
    }
    private int height(TreeNode t) {
        if (t == null) {
            return 0;
        }
        return 1 + Math.max(height(t.left), height(t.right));
    }
}
