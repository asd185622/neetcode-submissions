class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num:nums){
            if (!set.contains(num)){
                set.add(num);
            }
        }
        List<Integer> start = new ArrayList<>();
        for(int num:nums){
            if(!set.contains(num - 1)){
                start.add(num);
            }
        }
        int res = 0;
        for(int i = 0;i < start.size();i++){
            int length = 0;
            while(set.contains(start.get(i) + length)){
                length++;
            }
            res = Math.max(res,length);
        }
        
        // System.out.println(start);
        return res;
    }
}
