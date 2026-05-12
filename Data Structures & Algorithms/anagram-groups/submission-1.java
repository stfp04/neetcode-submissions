class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        List<Map<Character, Integer>> charList = new ArrayList<>();
        Set<Integer> seen = new HashSet<>();
        for(int i = 0; i < strs.length; i++) {
            Map<Character, Integer> curr = new HashMap<>();
            String tmp = strs[i];
            for(int j = 0; j < tmp.length(); j++) {
                char ch = tmp.charAt(j);
                if(curr.containsKey(ch)) {
                    int val = curr.get(ch) + 1;
                    curr.replace(ch, val);
                }
                else {
                    curr.put(ch, 1);
                }
            }
            charList.add(curr);
        }

        for(int i = 0; i < charList.size(); i++) {
            if(seen.contains(i))
                continue;
            seen.add(i);

            Map<Character, Integer> mapi = charList.get(i);
            List<String> toAdd= new ArrayList<>();
            toAdd.add(strs[i]);
            for(int j = i + 1; j < charList.size(); j++) {
                if(seen.contains(j))
                    continue;

                Map<Character, Integer> mapj = charList.get(j);
                if(mapj.equals(mapi)) {
                    toAdd.add(strs[j]);
                    seen.add(j);
                }
            }
            res.add(toAdd);
        }
        return res;
    }
}
