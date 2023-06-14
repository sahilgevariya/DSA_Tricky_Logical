# LeetCode
  # https://leetcode.com/problems/minimum-distance-between-bst-nodes/
  # https://leetcode.com/problems/minimum-absolute-difference-in-bst/

### Excellent [Recursive] ###
def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    def fn(node, prev, next):
        if not node: 
            return next - prev
                            # reduce range instead of [-inf,inf] 
        left = fn(node.left, prev, node.val)
        right = fn(node.right, node.val, next)

        return min(left, right)
    return fn(root, float('-inf'), float('inf'))

#### In-Order [Recursive] ####
def getMinimumDifference(self, root):
    self.res = float('inf')
    self.prev = -float('inf')

    def inOrder(root):
        if root.left:
            inOrder(root.left)
        self.res = min(root.val - self.prev, self.res)
        self.prev = root.val
        if root.right:
            inOrder(root.right)

    inOrder(root)
    return self.res

#### In-Order [Iterative] ####
def minDiffInBST(self, root):
    stack = []
    curr = root
    prev = None
    minimum = float('inf')
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            if prev:
                minimum = min(minimum, curr.val - prev.val)
            prev = curr
            curr = curr.right
    return minimum
