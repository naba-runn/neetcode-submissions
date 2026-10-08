class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right=len(numbers)-1
        left=0
        while(left<right):
            num=numbers[left]+numbers[right]
            if num<target:
                left+=1
            elif num>target:
                right-=1
            else:
                return [left+1,right+1]
        