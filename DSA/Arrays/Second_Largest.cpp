/*Second Largest Element

Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

Examples:
Input: nums = [8, 8, 7, 6, 5]

Output: 7

Explanation:

The largest value in nums is 8, the second largest is 7
Input: nums = [10, 10, 10, 10, 10]

Output: -1

Explanation:

The only value in nums is 10, so there is no second largest value, thus -1 is returned

Input: nums = [7, 7, 2, 2, 10, 10, 10]

Constraints:
1 <= nums.length <= 10^5
-104 <= nums[i] <= 10^4
nums may contain duplicate  elements.

*/

class Solution {
public:
    int secondLargestElement(vector<int>& nums) {
        int First = INT_MIN;
        int Second = INT_MIN;
        for(int num : nums){
            if(num>First){
                Second=First;
                First=num;
            }
            else if(num<First && num>Second){
                Second=num;
            }
        }
        return (Second == INT_MIN)?-1 : Second;
    }
};
