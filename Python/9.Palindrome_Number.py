class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x < 0:
			return False

		if x < 10:
			return True
		
		str_x = str(x)
		result = True
		for i in range((len(str_x) + 1)//2):
			if str_x[i] != str_x[len(str_x) - 1 - i]:
				result = False
				break
			return result