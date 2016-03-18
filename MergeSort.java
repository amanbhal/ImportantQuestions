public class MergeSort{
    public void merge(int[] A, int[] temp, int left, int right){
        if(left<right) {
            int mid = (left+right)/2;
            merge(A,temp,left,mid);
            merge(A,temp,mid+1,right);
            mergeAux(A,temp,left,mid,right);
        }
    }

    public void mergeAux(int[] A, int[] temp, int left, int mid, int right){
        int len = right-left+1;
        int lptr = left;
        int rptr = mid+1;
        int ptr = left;
        while(lptr<=mid && rptr<=right){
            if(A[lptr]<A[rptr]){
                temp[ptr++] = A[lptr];
                lptr++;
            }
            else{
                temp[ptr++] = A[rptr];
                rptr++;
            }
        }
        while(lptr<=mid){
            temp[ptr++] = A[lptr];
            lptr++;
        }
        while(rptr<=right){
            temp[ptr++] = A[rptr];
            rptr++;
        }
        for(int i = 0; i < len; i++, right--)
            A[right] = temp[right];
    }
    public static void main(String[] args){
        int[] A = {5,4,3,2,1};
        int[] temp = new int[A.length];
        Solution sol = new Solution();
        sol.merge(A,temp,0,A.length-1);
        for(int i=0; i<A.length; i++)
            System.out.println(A[i]);
    }
}