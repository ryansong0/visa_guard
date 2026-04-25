import java.util.*;

public class AllPaths {
    public String[] paths(TreeNode t) {
        List<String> result = new ArrayList<>();
        if (t != null) {
            find(t, "" + t.info, result);
        }
        Collections.sort(result);
        return result.toArray(new String[0]);
    }

    private void find(TreeNode node, String current, List<String> result) {
        if (node.left == null && node.right == null) {
            result.add(current);
            return;
        }
        if (node.left != null) {
            find(node.left, current + "->" + node.left.info, result);
        }
        if (node.right != null) {
            find(node.right, current + "->" + node.right.info, result);
        }
    }
}