import java.util.*;

class Solution {
    public long solution(int[] sequence) {
        List<Long> sequenceArray = new ArrayList<>();
        for(int ele : sequence){
            sequenceArray.add((long) ele);
        }
        List<Long> arr1 = new ArrayList<>();
        List<Long> arr2 = new ArrayList<>();
        
        for(int i=0;i<sequenceArray.size();i++){
            if(i%2==0){
                arr1.add(sequenceArray.get(i));
                arr2.add(sequenceArray.get(i)*(-1));
            }
            else{
                arr1.add(sequenceArray.get(i)*(-1));
                arr2.add(sequenceArray.get(i));
            }
        }
        List<Long> result1 = new ArrayList<>();
        List<Long> result2 = new ArrayList<>();
        result1.add(arr1.get(0));
        result2.add(arr2.get(0));
        
        for(int i=1;i<arr1.size();i++){
            result1.add(Math.max( arr1.get(i) + result1.get(i-1), arr1.get(i)));
            result2.add(Math.max( arr2.get(i) + result2.get(i-1), arr2.get(i)));
        }
        // System.out.println(arr1);
        // System.out.println(result1);
        // System.out.println(arr2);
        // System.out.println(result2);
        return Math.max(Collections.max(result1),Collections.max(result2));
    }
}
