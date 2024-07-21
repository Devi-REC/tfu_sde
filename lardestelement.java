
class Solution {
    public static int largest(int n, int[] arr) {
        // code here
        int a=arr[0];
        for(int i=1;i<n;i++){
            if(arr[i]>a){
                a=arr[i];
            }
        }
        return a;
    }
}
