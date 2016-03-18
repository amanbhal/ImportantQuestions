class TreeNode{
    int val;
    TreeNode left;
    TreeNode = right;
    public TreeNode(int value){
        val = value;
    }
}
public class InvertBT{
    public void invertBT(TreeNode root){
        if(root==null)
            return;
        invertBT(root.left);
        invertBT(root.right);
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
    }

    public static void main(String[] args){
        InvertBT sol = new InvertBT();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.right.left = new TreeNode(5);
        sol.invertBT(root);
        System.out.println(root.left.val);
    }
}