import java.util.*;

public class PathSum {
        public int hasPath(int target, TreeNode tree) {
    if (tree == null) return 0;

    if (tree.left == null && tree.right == null) {
        if (tree.info == target) {
            return 1;
        }
        else {
            return 0;
        }
    }

    int remain = target - tree.info;

    if (tree.left != null) {
        if (hasPath(remain, tree.left) == 1) {
            return 1;
        }
    }

    if (tree.right != null) {
        if (hasPath(remain, tree.right) == 1) {
            return 1;
        }
    }

    return 0;
}
}