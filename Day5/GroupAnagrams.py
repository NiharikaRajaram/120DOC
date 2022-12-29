class Solution:
     def findPrimeProduct(self, word, prime_map):
        product = 1
        for char in word:
            val = prime_map[ord(char) - ord('a')]
            product *= val
        return product
        
     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs ==  None or len(strs) == 0:
            return []
        
        # use prime numbers to get prime products
        prime_map = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        
        result = {}
        
        for word in strs:
            prime_product = self.findPrimeProduct(word, prime_map)
            
            if prime_product not in result:
                result[prime_product] = []
            result[prime_product].append(word)                
            
        return result.values()

# Alternative method - sort strings and store original words in a dictionary.  Return the dictionary values.