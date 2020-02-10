
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		usedChar = {}
		start = maxLen = 0

		for i in range(len(s)):
			if s[i] in usedChar and start <= usedChar[s[i]]:
				start = usedChar[s[i]] + 1
			else:
				maxLen = max(maxLen, i - start + 1)
			usedChars[s[i]] = i
		return maxLen


