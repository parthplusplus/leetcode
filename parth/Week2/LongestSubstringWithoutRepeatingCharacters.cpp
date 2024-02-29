// abdbca
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> umap;
        int start = 0;
        int longest = 0;
        for(int i=0;i<s.size();i++)
        {
            if(umap.contains(s[i]) && umap[s[i]]>=start)
            {
                start = umap[s[i]]+1;
            }
            umap[s[i]] = i;
            longest = max(longest, i-start+1);
        }
        return longest;
    }
};