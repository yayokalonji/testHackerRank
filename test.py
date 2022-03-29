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

print (gradingStudents([70 ,74, 73, 67, 38, 51, 33]))


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


countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])

def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        print ("YES")
    else:
        print ("NO")

kangaroo(0, 2, 3, 3)

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

print(getTotalX([2,4], [16, 32,96]))