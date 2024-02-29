class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::vector<std::vector<int>> sol;
        std::sort(nums.begin(), nums.end());
        for(int i=0; i<nums.size(); i++)
        {
            for(int j=i+1,k=nums.size()-1;j<k;)
            {
                long sum = nums[j] + nums[k] + nums[i];
                if(sum == 0)
                {
                    std::vector<int> triplet;
                    triplet.push_back(nums[i]);
                    triplet.push_back(nums[j]);
                    triplet.push_back(nums[k]);
                    sol.push_back(triplet);
                    j++;
                    k--;
                    while(j<nums.size() && nums[j] == nums[j-1])
                    {
                        j++;
                    }
                    while(k>=0 && k+1<nums.size() && nums[k] == nums[k+1])
                    {
                        k--;
                    }
                } 
                else if(sum > 0)
                {
                    k--;
                } 
                else if (sum < 0)
                {
                    j++;
                }
            }
            while(i+1 < nums.size() && nums[i] == nums[i+1])
            {
                i++;
            }
        }
        return sol;
    }
};