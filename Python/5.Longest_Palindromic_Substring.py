class Solution:
	def longestPalindrome(self, s: str) -> str:
		if len(s) == 0:
			return s
		max_str = s[0]

		for i in range(len(s)):
			# odd
			str1 = self.check(s, i, i)
			# even
			str2 = self.check(s, i, i+1)
			if len(max_str) < max(len(str1), len(str2)):
				if len(str1) > len(str2):
					max_str = str1
				else:
					max_str = str2
		return max_str

	def check(self, s:str, l:int, r:int) -> str:
		while l >= 0 and r < len(s) and s[l] == s[r]:
			l -= 1
			r += 1
		return s[l+1: r]