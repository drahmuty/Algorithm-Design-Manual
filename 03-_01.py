# Jolly Jumpers

# input: array of numbers
# output: true or false for jolly or not jolly

# create a hash table of each number 1 to n-1
# calculate abs(difference) between each number
# if difference is greater than n-1, return false
# search for that calcuulated value in the hash table
# if it's in the table, remove that value from the table
# if it's not in the table, return false
# if end of array, return true
# O(n) runtime and O(n) space

def jolly(nums):
    nums_len = len(nums)
    nums_arr = [True for i in range(nums_len)]
    i = 0
    while i < (nums_len - 1):
        curr_num = nums[i]
        next_num = nums[i + 1]
        diff = abs(curr_num - next_num)
        if diff > (nums_len - 1):
            return False
        elif nums_arr[diff] == True:
            nums_arr[diff] = False
            i += 1
        else:
            return False
    nums_arr.pop(0)
    if True in nums_arr:
        return False
    else:
        return True

print(jolly([1,2]))
print(jolly([1,2,4]))
print(jolly([1,2,4,7,11]))
print(jolly([-7,-5,-6]))
print(jolly([6,3,1,8,4,1,6,12]))
