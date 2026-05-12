#include <unordered_set>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> uset;
        for(int i = 0; i < nums.size(); i++) {
            if(uset.count(nums[i]))
                return true;
            uset.insert(nums[i]);
        }
        return false;
    }
};