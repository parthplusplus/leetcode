class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string,vector<string>> umap;
        for(string& s: strs)
        {
            string hashKey = string(s);
            sort(hashKey.begin(), hashKey.end());
            if (!umap.contains(hashKey))
            {
                umap.insert({hashKey, vector<string>()});
            }
            umap[hashKey].push_back(s);
        }
        for(auto& p : umap)
        {
            result.push_back(p.second);
        }
        return result;
    }
};