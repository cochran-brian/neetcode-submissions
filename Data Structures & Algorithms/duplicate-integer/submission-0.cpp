class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            if (m[nums[i]]) {
                return true;
            } else {
                m[nums[i]] = 1;
            }
        }

        return false;
    }
};