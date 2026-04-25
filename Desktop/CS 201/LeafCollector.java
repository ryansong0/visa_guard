import java.util.*;

public class LeafCollector {
    public String[] getLeaves(TreeNode tree) {
        List<String> rounds = new ArrayList<>();
        
        while (tree != null) {
            List<Integer> currentleave = new ArrayList<>();
            
            tree = remove(tree, currentleave);
            
            String val = "";
            for (int i = 0; i < currentleave.size(); i++) {
                val += currentleave.get(i);
                
                if (i < currentleave.size() - 1) {
                    val += " ";
                }
            }
            rounds.add(val);
        }
        return rounds.toArray(new String[0]);
    }

    private TreeNode remove(TreeNode node, List<Integer> leaves) {
        if (node == null) {
            return null;
        }
        if (node.left == null && node.right == null) {
            leaves.add(node.info);
            return null;
        }
        node.left = remove(node.left, leaves);
        node.right = remove(node.right, leaves);

        return node;
    }
}