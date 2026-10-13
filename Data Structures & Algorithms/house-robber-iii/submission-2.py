class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {None: 0}

        def dfs(cur):
            if cur in cache:
                return cache[cur]

            # Option 1: rob cur, so skip its children
            rob_cur = cur.val

            if cur.left:
                rob_cur += dfs(cur.left.left)
                rob_cur += dfs(cur.left.right)

            if cur.right:
                rob_cur += dfs(cur.right.left)
                rob_cur += dfs(cur.right.right)

            # Option 2: don't rob cur
            skip_cur = dfs(cur.left) + dfs(cur.right)

            cache[cur] = max(rob_cur, skip_cur)
            return cache[cur]

        return dfs(root)