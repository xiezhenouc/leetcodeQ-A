'''
count and say
'''
class Solution(object):
    def countAndSay(self, n):
        result = []
        result.append('1')

        k = 1
        while k < n:
            curstr = ''
            i = 0
            while i < len(result[k-1]):
                count = 1
                ch = result[k-1][i]
                while i + 1 < len(result[k-1]) and result[k-1][i] == result[k-1][i+1]:
                    count += 1
                    i += 1
                curstr += str(count) + ch
                i += 1
            result.append(curstr)

            k += 1
        return result[n-1]
if __name__ == '__main__':
    n = 10
    print Solution().countAndSay(n)
