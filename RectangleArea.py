# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
# Rectangle Area
# Assume that the total area is never beyond the maximum possible value of int.
#
# https://leetcode.com/problems/rectangle-area/#/description

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int first left
        :type B: int first bottom
        :type C: int first right
        :type D: int first top
        :type E: int second left
        :type F: int second bottom
        :type G: int second right
        :type H: int second top
        :rtype: int
        """
        total = (C-A)*(D-B) + (G-E)*(H-F)
        if (C <= E) or (A >= G) \
                or B >= H or D <= F:
            return total

        left = max(A, E)
        right = min(C,G)
        top = min(D,H)
        bottom = max(B,F)

        return total - (right - left)*(top - bottom)

s = Solution()
print(s.computeArea(-3,0,3,4,0,-1,9,2))