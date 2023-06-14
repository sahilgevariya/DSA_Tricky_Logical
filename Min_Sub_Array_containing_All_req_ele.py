# LeetCode : https://leetcode.com/problems/minimum-window-substring/

# TC = SC = O(n)
def minWindow(self, s: str, t: str) -> str:
      need = Counter(t)
      req_match = len(t)
      min_len = len(s)
      ans = ''

      l,r = 0,0
      while r < len(s):
          if s[r] in need:
              # s = ABBC, t = ABC then for second B we won't have to decrease req_match
              # but we have two B's in our window so reduce need (have extra)
              need[s[r]] -= 1
              if need[s[r]] >= 0:
                  req_match -= 1

              # check if our window found all required chars
              if req_match == 0:
                  # reduce left end until we required some char to search
                  while req_match == 0:
                      # add that char to need bucket again
                      if s[l] in need:
                          need[s[l]] += 1
                          # increase req_match, iff window contain only required chars
                          # not more that required 
                          if need[s[l]] > 0:
                              req_match += 1

                              if (r-l+1) <= min_len:
                                  ans = s[l:r+1]
                                  min_len = (r-l+1)

                      l += 1
          # increase right side every time
          r += 1

      return ans
    
'''
Output:
  s = "ADOBECODEBANC"
  t = "ABC"

  "BANC"
'''
