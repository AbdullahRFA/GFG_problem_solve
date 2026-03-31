class Solution:
    def nextGreaterElement(self,nums):
        n = len(nums)
        result = [-1]*n
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]<nums[j]:
        #             result[i]=nums[j]
        #             break
        
        stack = []
        
        for i in range(-1,-n-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            if stack:
                result[i]=stack[-1]
            stack.append(nums[i])
                    
        return result
                    
                    
slv = Solution()
nums = list(map(int,input("Enter the number separeted by space: ").split(' ')))
print(slv.nextGreaterElement(nums))