class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for(int num : nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        // System.out.println(map.entrySet());
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
            int freq = entry.getValue();
            int num = entry.getKey();
            heap.offer(new int[]{freq,num});
        }
        while(heap.size() > k){
            heap.poll();
        }
        int[] res = new int[k];
        for(int i=0;i<k;i++){
            res[i] = heap.poll()[1];
        }

        return res;
    }
}
