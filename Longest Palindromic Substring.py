#leetcoe 5 가장 긴 팰린드롬 문자열
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        #
        def expand_Palindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]
        
        for i in range(len(s)):
            odd_palindrome = expand_Palindrome(s,i,i)
            even_palindrome = expand_Palindrome(s,i,i+1)

            if len(odd_palindrome) > len(answer):
                answer = odd_palindrome
            if len(even_palindrome) > len(answer):
                answer = even_palindrome
        
        return answer