class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();

        for(String str: strs){
            int[] tmp = new int[26];
            char[] ch = str.toCharArray();
            for(char c : ch){
                tmp[c - 'a'] += 1;
            }
            String key = Arrays.toString(tmp);
            if(map.containsKey(key)){
                map.get(key).add(str);
            }else{
                List<String> tmpList = new ArrayList<>();
                tmpList.add(str);
                map.put(key,tmpList);
            }
        }
        return new ArrayList<>(map.values());
    }
}
