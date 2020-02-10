class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1
		m, n = len(nums1), len(nums2)

		half_size = (m + n + 1)//2
		start = 0
		end = m
		is_even = (len(nums1) + len(nums2))%2 == 0
		while start <= end:
			a_part = (start + end)//2
			b_part = half_size - a_part

			aleftmax = float("-INF") if a_part == 0 else nums1[a_part-1]
			arightmin = float("INF") if a_part == m else nums1[a_part]
			bleftmax = float("-INF") if b_part == 0 else nums2[b_part-1]
			brightmin = float("INF") if b_part == n else nums2[b_part]

			# right
			if aleftmax <= brightmin and bleftmax <= arightmin:
				if not is_even:
					return max(aleftmax, bleftmax)
				else:
					return (max(aleftmax, bleftmax), min(arightmin, brightmin))/2
			# move left
			elif aleftmax > brightmin:
				end = a_part-1
			# move right
			elif bleftmax > arightmin:
				start = a_part+1