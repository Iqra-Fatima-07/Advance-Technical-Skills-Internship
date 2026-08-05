/*
1752. Check if Array Is Sorted and Rotated

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums

Constraints:

1 <= nums.length <= 100
1 <=  nums[i] <= 100
*/

class Solution {
public:
    bool check(vector<int>& nums) {
        int count = 0;          // 'count' rakhega kitni baar array ka order break ho raha hai (descending point)
        int n = nums.size();    // array ka size nikal liya

        // Array ke elements ko pairwise check kar rahe hain
        for (int i = 0; i < n - 1; i++) {
            // Agar current element next se bada hai, matlab yahan rotation ya descending break hua
            if (nums[i] > nums[i + 1]) {
                count++;        // break count badha do
            }
        }

        // Ab circular case check karte hain (last aur first element ke beech)
        // Agar last element first se bada hai, toh ek aur break ho gaya
        if (nums[n - 1] > nums[0]) {
            count++;
        }

        // Agar count <= 1 hai, matlab array ya toh sorted hai
        // ya ek rotation se sorted ban sakta hai (allowed condition)
        return count <= 1;
    }
};