'''
set C, target T
for example :
    C:2 3 6 7     T:7 
    return [7], [2, 2, 3]
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        return self.myComSum(candidates, target, 0)

    def myComSum(self, candidates, target, start):
        result = []
        candidates.sort()

        i = start
        while i < len(candidates):
            if target - candidates[i] > 0:
                backresult = self.myComSum(candidates, target - candidates[i], i)
                for one in backresult:
                    one.insert(0, candidates[i])
                    result.append(one)
            elif target - candidates[i] == 0:
                singlelist = []
                singlelist.append(candidates[i])
                result.append(singlelist)
            else:
                break
            i += 1
        return result

if __name__ == '__main__':
    candidates = [11,10,5,7,8,12,3]
    target = 29
    print Solution().combinationSum(candidates, target)
