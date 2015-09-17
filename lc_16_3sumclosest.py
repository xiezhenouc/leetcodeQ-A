'''
3 sum closest
'''

def find3sumclosest(myset, target):
    mysetlen = len(myset)
    if mysetlen < 3:
        return None

    resultsum = 0
    resultdiff = 10000 
    
    myset.sort()
    i = 0
    while i < mysetlen:
        left = i + 1
        right = mysetlen - 1
        
        while left < right:
            if myset[i] + myset[left] + myset[right] < target:
                if resultdiff > abs(myset[i] + myset[left] + myset[right] - target):
                    resultsum =  myset[i] + myset[left] + myset[right]
                    resultdiff = abs(myset[i] + myset[left] + myset[right] - target)
                left += 1
            elif myset[i] + myset[left] + myset[right] > target:
                if resultdiff > abs(myset[i] + myset[left] + myset[right] - target):
                    resultsum =  myset[i] + myset[left] + myset[right]
                    resultdiff = abs(myset[i] + myset[left] + myset[right] - target)
                right -= 1
            else:
                resultsum = myset[i] + myset[left] + myset[right]
                resultdiff = 0
                break
                
        if resultdiff == 0:
            return resultsum 

        i += 1
    return resultsum

if __name__ == '__main__':
    myset = [0, 0, 0]
    print find3sumclosest(myset, 1)
