/*
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
*/


class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;  
        // 'result' ko 0 se initialize kiya. Yeh variable XOR result store karega.

        for (int num : nums) {
            // Har element ke liye loop chalega
            result ^= num;  
            // XOR operation: same number 2 baar aayega toh cancel ho jaata hai (a ^ a = 0)
            // Aur 0 ke saath XOR karne par number wahi rehta hai (a ^ 0 = a)
            // Toh end mein sirf wahi number bachega jo single hai.
        }

        return result;  
        // Single (unique) number return karo
    }
};
