import java.util.List;

class Solution {
    public int print2largest(List<Integer> arr) {
        // Code Here
         int first_large=arr.get(0);
         int second_large=-1;
         for(int i=0;i<arr.size();i++){
             if(arr.get(i)>first_large){
                 second_large=first_large;
                 first_large=arr.get(i);
             }
              else if(arr.get(i)<first_large && arr.get(i)>second_large){
                 second_large=arr.get(i);
             }
         }
         return second_large;
    }
}