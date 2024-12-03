class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> uset(nums.begin(), nums.end());
        int longest = 0;
        for(int& n : nums)
        {
            if(uset.contains(n-1))
            {
                continue;
            }
            int currentLongest = 0;
            while(uset.contains(n))
            {
                currentLongest++;
                uset.erase(n);
                n++;
            }
            if(longest < currentLongest)
            {
                longest = currentLongest;
            }
        }
        return longest;
    }
};