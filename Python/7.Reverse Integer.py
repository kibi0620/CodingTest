
class Solution:
    def reverse(self, x:int) -> int:
        if x == 0:
            return 0;
           
        sign = 0;
		if x < 0:
			sign = 1;
			x = abs(x);
			
		result = 0;
		while (x != 0):
			result *= 10;
			result += x % 10;
			x //= 10;
		
		# result > 0x7FFFFFFF
		if result > ((1<<31)-1) or (sign == 1 and result > ((1<<31)-1)):
			return 0;
			
		if (sign == 1) :
			result = -result;
		return result;
