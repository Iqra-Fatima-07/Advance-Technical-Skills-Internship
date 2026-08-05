/*
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 
*/

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();  // nums ka size store kar liya
        if (n == 0) return;   // agar array empty hai, return kar do
        k = k % n;            // agar k > n hai, to unnecessary rotations avoid karne ke liye modulo liya

        reverse(nums.begin(), nums.end());             // poore array ko reverse kar do
        reverse(nums.begin(), nums.begin() + k);      // pehle k elements ko reverse kar do (ye final rotated front banenge)
        reverse(nums.begin() + k, nums.end());        // baaki ke elements ko reverse kar do (ye final rotated back banenge)
    }
};
