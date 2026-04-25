import java.util.*;

public class TreeToList {
    public ListNode convert(TreeNode tree) {
        if (tree == null) {
            return null;
        }
        ListNode left = convert(tree.left);
        ListNode right = convert(tree.right);

        ListNode now = new ListNode(tree.info);
        now.next = right;

        if (left == null) {
            return now;
        }
        else {
            ListNode end = left;
            while (end.next != null) {
                end = end.next;
            }
            end.next = now;
            return left;
        }
    }
}
