from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        ans = []
        q = deque()
        q.append(root)

        while q:
            level = []
            n = len(q)

            for _ in range(n):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level)

        return ans