class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string out = "";
        for(int i=0; i<min(word1.size(), word2.size()); i++){
            out += word1[i];
            out += word2[i];
        }
        if(word1.size() > word2.size()){
            out += word1.substr(word2.size());
        }
        if(word2.size() > word1.size()){
            out += word2.substr(word1.size());
        }
        return out;
    }
};
