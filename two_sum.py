from typing import List


class Solution:
    nums = [3,2,4]
    target = 6
    def twoSum(nums: List[int], target: int) -> List[int]:
        prevNum = 0;
        newNum = 0;
        for idx,num in enumerate(nums):
            prevNum = num
            if(idx == 0):
                continue
            for id,childNum in enumerate(nums):
              if(id == idx):
                continue
              newNum = childNum;
              if((prevNum +newNum) == target):
                  return [idx,id];
            prevNum = newNum;
    print(twoSum(nums, target))

print(prevNum,newNum)

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/