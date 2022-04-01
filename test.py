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

bonAppetit([3,10,2,9], 1, 12)

