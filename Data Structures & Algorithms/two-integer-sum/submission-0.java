class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> sums = new HashMap<>();
        int[] res = new int[2];

        for(int i = 0; i < nums.length; i++) {
            int value = nums[i];
            int tmp = target - value;

            if(!sums.containsKey(tmp)) {
                sums.put(value, i);
            } else {
                res[0] = sums.get(tmp);
                res[1] = i;
                return res;
            }
        }
        return res;
    }
}
