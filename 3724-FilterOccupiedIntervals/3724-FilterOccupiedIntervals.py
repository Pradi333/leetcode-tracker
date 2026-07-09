# Last updated: 7/9/2026, 10:06:12 AM
class Solution(object):
    def filterOccupiedIntervals(self, occupiedIntervals, freeStart, freeEnd):
      if not occupiedIntervals:
          return[]
      occupiedIntervals.sort()
      merged=[]
      s,e= occupiedIntervals[0]
      for ns,ne in occupiedIntervals[1:]:
          if ns<=e+1:
              e=max(e,ne)
          else:
              merged.append([s,e])
              s,e=ns,ne
      merged.append([s,e])
      ans= []


      for l,r in merged:
          if r<freeStart or l>freeEnd:
              ans.append([l,r])
          else:
              if l<freeStart:
                  ans.append([l,freeStart-1])
              if r>freeEnd:
                  ans.append([freeEnd+1,r])
      return ans