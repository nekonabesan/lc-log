class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a1 = []
        a2 = []
        index = 0

        if m == 0 and n == 0:
            return nums1
        elif m == 0 and n != 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return nums1
        elif m != 0 and n == 0:
            return nums1

        for i in range(m):
            a1.append(nums1[i])

        for i in range(n):
            a2.append(nums2[i])
        
        while len(a1) > 0 and len(a2) > 0:
            if a1[0] <= a2[0]:
                nums1[index] = a1.pop(0)
                index = index + 1
            else:
                nums1[index] = a2.pop(0)
                index = index + 1


        if len(a1) > 0:
            while len(a1) > 0:
                nums1[index] = a1.pop(0)
                index = index + 1

        if len(a2) > 0:
            while len(a2) > 0:
                nums1[index] = a2.pop(0)
                index = index + 1
                    
        return nums1