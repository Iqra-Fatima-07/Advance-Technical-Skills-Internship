/*

485. Max Consecutive Ones
Solved
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.*/

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxi = 0;   // ab tak ka maximum consecutive 1s count store karega
        int count = 0;  // current consecutive 1s ko track karega
        
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] == 1) {        // agar current element 1 hai
                count++;              // to consecutive 1s ka count badha do
                maxi = max(maxi, count); // aur maximum ke sath compare karke update karo
            } 
            else {                    // agar 0 mil gaya
                count = 0;            // to consecutive count reset kar do
            }
        }
        return maxi; // last me maximum consecutive 1s return karo
    }
};
