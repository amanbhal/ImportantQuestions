/*
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
*/

//=>  Use priorityQueue to store the starting of each sorted list. PriorityQueue will automatically
//    sort them, then choose the smallest one from them add it to the new list and add the next
//    of the smallest one to the queue. Repeat until queue is empty.

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.ArrayList;

public class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
  }

 public class MergeKsortedLL {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length==0)
            return null;
        PriorityQueue<ListNode> q = new PriorityQueue<ListNode>(lists.length,new Comparator<ListNode> () {
            public int compare(ListNode a, ListNode b){
                if(a.val>b.val)
                    return 1;
                else if(a.val==b.val)
                    return 0;
                else
                    return -1;
            }
        });
        //add first nodes of each linked list
        for(ListNode node:lists){
            if(node!=null)
                q.add(node);
        }
        // make a new linked list that will have elements in the desired sorted manner
        ListNode newHead = new ListNode(0);
        ListNode curr = newHead;
        while(q.size()>0){
            ListNode temp = q.poll();
            curr.next = temp;
            curr = temp;
            if(temp.next!=null)
                q.add(temp.next);
        }
        return newHead.next;
    }
}
