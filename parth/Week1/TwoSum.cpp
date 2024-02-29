class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> result;
        std::unordered_map<int, int> umap;
        for(int i=0; i<nums.size(); i++){
            if(umap.contains(target - nums[i])){
                result.push_back(i);
                result.push_back(umap[target-nums[i]]);
                break;
            }
            umap.insert({nums[i], i});
        }
        return result;
    }
};