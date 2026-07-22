from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g

                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slopes[(dx, dy)] += 1

            ans = max(ans, max(slopes.values()) + 1 if slopes else 1)

        return ans