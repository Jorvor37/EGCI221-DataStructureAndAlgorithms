class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        def merge(nums1, m, nums2, n):
            p1 = m - 1
            p2 = n - 1
            p = m + n - 1

            # Merge from the back
            while p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[p] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[p] = nums2[p2]
                    p2 -= 1
                p -= 1

            # Copy remaining elements from nums2 (if any)
            while p2 >= 0:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1
            }
};
