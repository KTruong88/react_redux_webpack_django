# Halfling Woolly Proudhoof is an eminent sheep herder. He wants to build a pen (enclosure) for his new flock of sheep. The pen will be rectangular and built from exactly four pieces of fence (so, the pieces of fence forming the opposite sides of the pen must be of equal length). Woolly can choose these pieces out of N pieces of fence that are stored in his barn. To hold the entire flock, the area of the pen must be greater than or equal to a given threshold X.
#
# Woolly is interested in the number of different ways in which he can build a pen. Pens are considered different if the sets of lengths of their sides are different. For example, a pen of size 1×4 is different from a pen of size 2×2 (although both have an area of 4), but pens of sizes 1×2 and 2×1 are considered the same.
#
# Write a function:
#
# class Solution { public int solution(int[] A, int X); }
#
# that, given a zero-indexed array A of N integers (containing the lengths of the available pieces of fence) and an integer X, returns the number of different ways of building a rectangular pen satisfying the above conditions. The function should return −1 if the result exceeds 1,000,000,000.
#
# For example, given X = 5 and the following array A:
#
#   A[0] = 1
#   A[1] = 2
#   A[2] = 5
#   A[3] = 1
#   A[4] = 1
#   A[5] = 2
#   A[6] = 3
#   A[7] = 5
#   A[8] = 1
#
#  (Missing some pics)
#
# the function should return 2. The figure above shows available pieces of fence (on the left) and possible to build pens (on the right). The pens are of sizes 1x5 and 2x5. Pens of sizes 1×1 and 1×2 can be built, but are too small in area. It is not possible to build pens of sizes 2×3 or 3×5, as there is only one piece of fence of length 3.
# 1x5 and 2x5
#
# Assume that:
#
# N is an integer within the range [0..100,000];
# X is an integer within the range [1..1,000,000,000];
# each element of array A is an integer within the range [1..1,000,000,000].
# Complexity:
#
# expected worst-case time complexity is O(N*log(N));
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.

from collections import Counter


def solution(array_of_stick_lengths, minimum_area_needed):
    if array_of_stick_lengths and minimum_area_needed:
        possibilities = 0
        counted_sticks = Counter(array_of_stick_lengths)
        lotsa_sticks = [_stick for _stick in counted_sticks if counted_sticks[_stick] >= 4]  # for sticks of numbers great enough to build a 4 sided pen with that size alone
        valid_sticks = [stick for stick in counted_sticks if counted_sticks[stick] >= 2]  # # for sticks of numbers great enough to build a 4 sided pen with 2 different sizes
        if lotsa_sticks:
            for s in lotsa_sticks:
                if s * s >= minimum_area_needed:
                    possibilities += 1
        if valid_sticks:
            for i in valid_sticks:
                for k in valid_sticks:
                    if i != k and i * k >= minimum_area_needed:
                        print('i, k: ', i, k)
                        possibilities += 1
        print('answer: ', int(possibilities/2))
        return int(possibilities/2)


solution([1, 2, 5, 1, 1, 2, 3, 5, 1], 5)


# def solution(A, X):
#     fence_count = {}
#     for fence in A:
#         fence_count[fence] = fence_count.get(fence, 0) + 1
#
#     num_of_pens = 0
#     usable_fences = []
#     for fence in fence_count:
#         if fence_count[fence] < 2:
#             # Less than one pair. We cannot use it.
#             continue
#         elif fence_count[fence] < 4:
#             usable_fences.append(fence)
#         else:
#             usable_fences.append(fence)
#             # We consider the square pen here.
#             if fence * fence >= X:
#                 num_of_pens += 1
#
#     # We consider the non-square pen here.
#     usable_fences.sort()
#     candidate_size = len(usable_fences)
#     for i in xrange(candidate_size):
#         # Use binary search to find the first fence pair, that
#         # could be used with current pair to form a pen.
#         begin = i + 1
#         end = candidate_size - 1
#         while begin <= end:
#             mid = (begin + end) // 2
#             if usable_fences[mid] * usable_fences[i] >= X:
#                 end = mid - 1
#             else:
#                 begin = mid + 1
#
#         # Now the usable_fences[end + 1] is the first qualified
#         # fence.
#         combination_num = candidate_size - (end + 1)
#         num_of_pens += combination_num
#         if num_of_pens > 1000000000:
#             return -1
#
#     return num_of_pens
