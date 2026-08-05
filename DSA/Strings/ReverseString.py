class Solution:
    def reverseString(self, s: str) -> str:
        return s[::-1]

#OR

class Solution:
    def reverseString(self, s: list[str]) -> None:
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

#C++ code
'''
class Solution {
public:
    void reverseString(vector<char>& s) {
        int i = 0;
        int j = s.size() - 1;

        while (i < j) {
            swap(s[i], s[j]);
            i++;
            j--;
        }
    }
};
'''