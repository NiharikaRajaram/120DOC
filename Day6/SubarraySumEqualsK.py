class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        dict = {0: 1}
        rSum = 0

        for num in nums:
            # running Sum
            rSum += num

            # difference between k and running Sum
            diff = rSum - k
            if diff in dict.keys():
                count += dict[diff]
                
            if rSum in dict:
                dict[rSum] += 1
            else:
                dict[rSum] = 1
    
        return count