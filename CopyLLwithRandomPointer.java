/*
A linked list is given such that each node contains an additional random pointer which could point to
any node in the list or null.

Return a deep copy of the list.
*/

//=>  we maintain a hashMap in which we store the nodes in new list corresponding to the nodes in old
//    list.

class RandomListNode {
      int label;
      RandomListNode next, random;
      RandomListNode(int x) { this.label = x; }
  };

public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if(head==null)
            return null;
        HashMap<RandomListNode,RandomListNode> map = new HashMap<RandomListNode,RandomListNode>();
        RandomListNode newHead = new RandomListNode(head.label);
        RandomListNode p = head;
        RandomListNode q = newHead;
        map.put(p,q);
        p = p.next;
        while(p!=null){
            RandomListNode temp = new RandomListNode(p.label);
            map.put(p,temp);
            q.next = temp;
            q = temp;
            p = p.next;
        }
        p = head;
        q = newHead;
        while(p!=null){
            if(p.random!=null)
                q.random = map.get(p.random);
            else
                q.random = null;
            p = p.next;
            q = q.next;
        }
        return newHead;
    }
}
