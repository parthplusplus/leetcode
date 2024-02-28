class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> dups;
        for(int& n : nums){
            if(!dups.insert(n).second){
                return true;
            }
        }
        return false;
    }
};