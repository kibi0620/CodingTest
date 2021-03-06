class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		dp = [[False]*(len(s)+1) for _ in (len(p)+1)]
		dp[0][0] = True
		for i in range(len(p)+1):
			dp[i+1][0] = dp[i-1][0] and p[i] == '*'
		for i in range(len(p)):
			for j in range(len(s)):
				if p[i] == '*':
					dp[i+1][j+1] = dp[i-1][j+1] or dp[i][j+1]
					if p[i-1] == s[j] or p[i-1] == '.':
						dp[i+1][j+1] |= dp[i+1][j]
				else:
					dp[i+1][j+1] = dp[i][j] or (p[i] == '.' or p[i] == s[j])
		return dp[-1][-1]
