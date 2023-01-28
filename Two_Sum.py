class Solution(object):
    def twoSum(self, nums, target):
        x=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (target==nums[i]+nums[j]):
                    x.append(i)
                    x.append(j)
                    return x
        