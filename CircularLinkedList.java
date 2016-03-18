class ListNode{
    int val;
    ListNode next;
    public ListNode(int value){
        val = value;
    }
}
public class CircularLinkedList{
    ListNode head = null;
    public void add(int value){
        ListNode temp = new ListNode(value);
        if(head==null){
            head = temp;
            head.next = head;
        }
        else{
            ListNode tail = head;
            while(tail.next!=head){
                tail = tail.next;
            }
            tail.next = temp;
            temp.next = head;
        }
    }
    public void delete(int value){
        if(head==null)
            return;
        ListNode prev = null;
        ListNode curr = head;
        while(curr.val!=value && curr.next!=head){
            prev = curr;
            curr = curr.next;
        }
        if(prev==null && curr.val==value){
            ListNode tail = head;
            while(tail.next!=head){
                tail = tail.next;
            }
            if(tail==head) {
                head = null;
                return;
            }
            tail.next = curr.next;
            head = curr.next;
        }
        else {
            prev.next = curr.next;
        }
    }

    public static void main(String[] args){
        Solution sol = new Solution();
        sol.add(1);
        sol.add(2);
        sol.add(3);
        sol.add(4);
        sol.add(5);
        sol.add(6);
        sol.delete(1);
        System.out.println(sol.head.val);
    }
}

