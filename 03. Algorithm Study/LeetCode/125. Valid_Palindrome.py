class Solution:
#     def isPalindrome(self, s: str) -> bool: # deque 사용
#         inputs = collections.deque()
#         for char in s:
#             if char.isalnum():
#                 inputs.append(char.lower())
                
#         while (len(inputs)) > 1:
#             if inputs.pop() != inputs.popleft():
#                 return False
        
#         return True
    def isPalindrome(self, s: str) -> bool: # slicing 사용
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        
        return s == s[::-1]
      
#https://leetcode.com/problems/valid-palindrome/
