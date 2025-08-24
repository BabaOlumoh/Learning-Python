#filter filters by using a function matched against the provided variable

def check_sum(nums):
    return nums % 2== 0

mynums = [1,2,3,4,5]

list(filter(check_sum,mynums))

for num in filter(check_sum, mynums):
    print(num)