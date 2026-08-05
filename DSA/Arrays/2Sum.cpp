/*1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;  
        // unordered_map use kar rahe hain jahan key = number, value = uska index store hoga
        // isse hum O(1) time me check kar sakte hain ki koi number pehle aa chuka hai ya nahi

        for (int i = 0; i < nums.size(); i++) {  
            // poore array ke elements par iterate karenge

            int complement = target - nums[i];  
            // har element ke liye complementary number nikal rahe hain
            // jo target banane ke liye zaroori hai

            if (mp.find(complement) != mp.end()) {  
                // agar complement map me already present hai
                // matlab pehle koi number aisa tha jo current number ke sath milke target deta hai
                
                return {mp[complement], i};  
                // toh dono ke indices return kar do
            }

            mp[nums[i]] = i;  
            // agar complement nahi mila toh current number aur uska index map me daal do
        }

        return {};  
        // agar koi pair nahi mila toh empty vector return kar do
    }
};

