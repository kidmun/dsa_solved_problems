def missingNumber(nums):
    
    n = len(nums) + 1
    
    total = n*(n+1)/2
   
    number = total - sum(nums)
    return number

