class Solution:
	cache = {}

	def isMatch(self, s: str, p: str) -> bool:
		if (s, p) in cache:
			return cache[(s, p)]
		if not p:
			return not s
		if p[-1] == '*':
			if self.isMatch(s, p[:-2]):
				self.cache[(s, p)] = True
				return True
			if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):
				self.cache[(s, p)] = True
				return True
		if s and (p[-1] == '.' or s[-1] == p[-1]) and self.isMatch(s[:-1], p[:-1]):
			self.cache[(s, p)] = True
			return True
		self.cache[(s, p)] = False
		return False