'''
find the longest common prefix string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        strslen = len(strs)
        if strslen < 1:
            return '' 

        minlen = len(strs[0]) 

        #find min string
        for onestr in strs:
            if minlen > len(onestr):
                minlen = len(onestr)
        print 'minlen ', minlen

        #find longest common prefix
        i = 0
        stop = 0
        while i < minlen:
            tmpch = strs[0][i]
            for onestr in strs:
                if tmpch != onestr[i]:
                    print 'i ', i
                    stop = 1
                    break

            if stop == 1:
                break

            i += 1

        return strs[0][0:i]

if __name__ == '__main__':
    strs = ['xiehaibao', 'xiezhen']

    print Solution().longestCommonPrefix(strs)
