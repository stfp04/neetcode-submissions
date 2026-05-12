class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 1, i = 1;
        while(i < nums.length) {
            if(nums[i] != nums[i - 1]) {
                nums[k++] = nums[i];
            }
            i++;
        }
        return k;
    }
}