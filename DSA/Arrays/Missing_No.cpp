/*
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

 

*/

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();  
        // 'n' mein total elements ka size store kar liya (actual numbers 0 to n tak hone chahiye)
        
        int xor1 = 0, xor2 = 0;  
        // xor1 = 0 to n tak ke numbers ka XOR store karega
        // xor2 = array ke andar ke elements ka XOR store karega

        for (int i = 0; i < n; i++) {
            xor2 ^= nums[i];      // array ke sab elements ka XOR lete ja rahe hain
            xor1 ^= (i + 1);      // 1 se n tak ke numbers ka XOR lete ja rahe hain
        }

        return xor1 ^ xor2;  
        // Dono XOR ko combine karne se missing number mil jaata hai
        // Kyunki same numbers cancel ho jaate hain (XOR property: a^a = 0)
        // Sirf missing number bacha rahta hai
    }
};
