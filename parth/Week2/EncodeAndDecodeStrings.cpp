class Codec {
private:
    const string delimiter = "|";
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string result;
        for(string& str : strs){
            result.append(to_string(str.size()));
            result.append(delimiter);
            result.append(str);
        }
        return result;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> result;
        for(int i=0; i<s.size();){
            int indexOfDelimiter = s.find(delimiter, i);
            int lenOfString = stoi(s.substr(i,indexOfDelimiter));
            result.push_back(s.substr(indexOfDelimiter+1,lenOfString));
            i=indexOfDelimiter+lenOfString+1;
        }
        return result;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));