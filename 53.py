class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxSubArrayab(a,low,high):
            r = []
            l = []
            m = []
            if low == high:
                return [low,high,a[low]]
            else:
                mid = int((low + high)/2)
                r = maxSubArrayab(a,low,mid)
                l = maxSubArrayab(a,mid+1,high)
                m = maxSubArrayc(a,low,mid,high)
                if r[2]>=l[2] and r[2]>=m[2]:
                    return r
                elif l[2]>=r[2] and l[2]>=m[2]:
                    return l
                else:
                    return m
        def maxSubArrayc(a,low,mid,high):
            max_l = -float('inf')
            max_r = -float('inf')
            sum = 0
            i = mid
            while i >= low:
                sum = sum + a[i]
                if sum >= max_l:
                    max_l = sum
                    l = i
                i = i -1
            sum = 0
            j = mid + 1
            while j <= high:
                sum = sum + a[j]
                if sum >= max_r:
                    max_r = sum
                    r = j
                j = j + 1
            return [l, r, max_l + max_r]
        ref = maxSubArrayab(nums, 0, len(nums) - 1)
        return ref[2]
