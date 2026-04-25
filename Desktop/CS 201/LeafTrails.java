import java.util.*;

public class LeafTrails {
    public String[] trails(TreeNode tree) {
        TreeMap<Integer, String> map = new TreeMap<>();
        find(tree, "", map);
        return map.values().toArray(new String[0]);
    }

    private void find(TreeNode node, String path, Map<Integer, String> map) {
        if (node == null) {
            return;
        }
        if (node.left == null && node.right == null) {
            map.put(node.info, path);
            return;
        }
        find(node.left, path + "0", map);
        find(node.right, path + "1", map);
    }
}