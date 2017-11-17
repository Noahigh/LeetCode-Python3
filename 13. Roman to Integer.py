# 13. Roman to Integer

# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

def NumCal(num):    
    n = 0
    for i in range(len(num)-1):
        if num[i] >= num[i+1]:
            n = n + num[i]
        else:
            n = n - num[i]
    n = n + num[-1]
    return n


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    romanDic = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }

    romanStrToList = list(s)

    num = []

    for i in range(len(romanStrToList)):
        num.append(romanDic[romanStrToList[i]])


    print(romanDic)
    print(romanStrToList)
    print(num)
    
    return num


num = romanToInt('DCXXI')
print(NumCal(num))

num = romanToInt('DCVXI')
print(NumCal(num))
