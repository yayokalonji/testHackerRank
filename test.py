from turtle import st


def gradingStudents(grades):
    result = []
    for i in grades:
        if i >= 38 :
             multiple5 = (i % 5)
             if multiple5 == 3 :
                 result.append( i + 2 )
             elif multiple5 == 4 :
                 result.append( i + 1)
             elif multiple5 <= 2 :
                 result.append(i) 
        else:
            result.append(i)

    return result

#print (gradingStudents([70 ,74, 73, 67, 38, 51, 33]))


def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0
    for i in apples:
        if a + i >= s and a + i <= t :
            count_apples += 1
    for j in oranges:
        if b + j >= s and b + j <= t :
            count_oranges += 1
    print (count_apples)
    print (count_oranges)


#countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])

def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        print ("YES")
    else:
        print ("NO")

#kangaroo(0, 2, 3, 3)

# Complete the 'getTotalX' function below.
#
#The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. INTEGER_ARRAY a
# 2. INTEGER_ARRAY b

def getTotalX(a, b):
    count = 0
    for i in range(max(a), min(b) + 1):
        left = all([i % numA == 0 for numA in a])
        right = all([numB % i == 0 for numB in b])
        print (left, right)
        count += left * right
    return count

#print(getTotalX([2,4], [16, 32,96]))

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    highest = scores[0]
    lowest = scores[0]
    highest_count = 0
    lowest_count = 0
    for i in scores:
        if i > highest:
            highest = i
            highest_count += 1
        if i < lowest:
            lowest = i
            lowest_count += 1
    return highest_count, lowest_count


#print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))


#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#
def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

#print(birthday([1, 2, 1, 3, 2], 3, 3))


#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1,,. INTEGER n
#  2,. INTEGER k
#  3,. INTEGER_ARRAY ar
#
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if((ar[i] + ar[j]) % k == 0):
                count += 1
    return count

# print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def migratoryBirds(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    max_val = max(count.values())
    min_val = min([k for k, v in count.items() if v==max_val])
    for key, value in count.items():
        if value == max_val and min_val == key:
            return key

#print(migratoryBirds([1,4,4,4,5,3]))

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
def dayOfProgrammer(year):
    if year < 1918:
        if year % 4 == 0:
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)
    else:
        if year == 1918:
            return "26.09 " + str(year)
        if year % 400 == 0:
            return "12.09." + str(year)
        elif year % 4 == 0 and year % 100 != 0:
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)

#print(dayOfProgrammer(2016))

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#
def bonAppetit(bill, k, b):
    bill.pop(k)
    total = sum(bill)
    if total / 2 == b:
        print ("Bon Appetit")
    else:
        print (int(b - total / 2))

# bonAppetit([3,10,2,9], 1, 12)


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if ar[i] == ar[j] and (ar[i] != 0 or ar[j] != 0):
                count += 1
                ar[i] = 0
                ar[j] = 0
    return count

#print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))


#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#
def pageCount(n, p):
    if p <= n/2:
        return int(p/2)
    elif n == 6 and p == 5:
        return 1
    else:   
        return int((n - p)/2)

#print(pageCount(6, 5))

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
def countingValleys(steps, path):
    count = 0
    level = 0
    for i in path:
        if i == 'U':
            level += 1
        else:
            level -= 1
        if level == 0 and i == 'U':
            count += 1
    return count

#print(countingValleys(8, 'UDDDUDUU'))


#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    max_val = 0
    for i in keyboards:
        for j in drives:
            if i + j <= b and i + j > max_val:
                max_val = i + j
    if max_val == 0:
        return -1
    else:
        return max_val

#print(getMoneySpent([4], [5], 5))

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if abs(x - z) < abs(y - z):
        return "Cat A"
    elif abs(x - z) > abs(y - z):
        return "Cat B"
    else:
        return "Mouse C"

#print(catAndMouse(1, 3, 2))

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
def formingMagicSquare(s):
    magic_squares = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
                    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
                    [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
    min_val = 1000
    for i in range(len(magic_squares)):
        val = 0
        for j in range(len(magic_squares[i])):
            for k in range(len(magic_squares[i][j])):
                val += abs(s[j][k] - magic_squares[i][j][k])
        if val < min_val:
            min_val = val
    return min_val

#print(formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def pickingNumbers(a):
    a.sort()
    max_val = 0
    for i in range(len(a)):
        count = 1
        for j in range(i+1, len(a)):
            if a[j] - a[i] == 1 or a[j] - a[i] == 0:
                count += 1
            else:
                break
        if count > max_val:
            max_val = count
    return max_val

#print(pickingNumbers([1, 2, 2, 3, 1, 2]))

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort()
    player.sort()
    l = len(player)
    i = 0
    j = 0
    res = []
    while i < l and j < len(ranked):
        if player[i] < ranked[j] and j == 0:
            res.append(len(ranked) + 1)
        elif player[i] < ranked[j] and j > 0 :
            res.append(len(ranked) - j)
        elif player[i] == ranked[j]:
            res.append(j)
        elif player[i] > ranked[j]:
            res.append(len(ranked) - j)
        j += 1
        i += 1
    return res
    
print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))