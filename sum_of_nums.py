

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_of_nums1(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
#3n+1 is big
#The bigger we grow the array 
#fn +1000(n)
#When you try to plot constant alfgorithm its a straight line that is constant
#Linear algorithm has a constant that's a slope
O (5n +3) - linear
O 5n**2 +3n + - quadrat
5n**3 + 1000n**2+10000n +1000000- cubic

result = sum_of_nums1(nums)
print(result)


def sum_of_nums2(nums):
    n = len(nums)
    sum = n *(n + 1)/2
    return sum

result =sum_of_nums2(nums)
print(result)