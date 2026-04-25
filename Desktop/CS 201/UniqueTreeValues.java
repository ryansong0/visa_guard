import java.util.*;

public class UniqueTreeValues {
    public int[] unique(TreeNode root) {
        TreeSet<Integer> set = new TreeSet<>();
        
        traverse(root, set);
        int[] result = new int[set.size()];
        int i = 0;
        for (Integer val : set) {
            result[i++] = val;
        }
        return result;
    }

    private void traverse(TreeNode node, Set<Integer> set) {
        if (node == null) {
            return;
        }
        set.add(node.info);
        traverse(node.left, set);
        traverse(node.right, set);
    }
}
