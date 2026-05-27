class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> m = {};

        for (unsigned int i = 0; i < nums.size(); ++i) {
            int dif = target - nums[i];

            if (m.count(dif) == 1) {
                return {m[dif], i};
            }

            m.insert({nums[i], i});
        }

        return {};
    }
};
