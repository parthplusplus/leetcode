class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size())
        {
            return false;
        }
        int freq[26];
        for(int i=0; i<s.size(); i++){
            freq[s[i]-'a']++;
        }
        for(int i=0; i<t.size(); i++){
            freq[t[i]-'a']--;
            if(freq[t[i]-'a'] < 0)
            {
                return false;
            }
        }
        return true;
    }
};