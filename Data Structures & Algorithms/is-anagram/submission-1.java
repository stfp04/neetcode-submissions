class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Integer, Integer> freq = new HashMap<>(); 
        int tmp;

        if(s.length() != t.length()) {
            return false;
        }

        for(int i = 0; i < s.length(); i++) {
            int c = s.charAt(i);
            if(freq.containsKey(c)) {
                tmp = freq.get(c) + 1;
                freq.replace(c, tmp);
            } else {
                freq.put(c, 1);
            }
        }

        for(int i = 0; i < t.length(); i++) {
            int c = t.charAt(i);
            if(freq.containsKey(c)) {
                tmp = freq.get(c) - 1;
                if(tmp == 0) {
                    freq.remove(c);
                } else {
                    freq.replace(c, tmp);
                }
            } else {
                return false;
            }
        }

        return freq.isEmpty();
    }
}
