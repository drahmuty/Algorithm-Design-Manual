# Jolly Jumpers

# input: array of numbers
# output: true or false for jolly or not jolly

# create a "hash table" array of each number 1 to n-1
# set each value in array to False
# calculate abs(difference) between each number
# if difference is greater than n-1, return false
# use difference as index into array
# if it's false (hasn't been used yet), set it to true and continue
# if it's not in the table, return false
# if end of array, return true
# O(n) runtime and O(n) space


def jolly(nums):
    nums_len = len(nums)
    nums_arr = [False for i in range(nums_len - 1)]
    i = 0
    while i < (nums_len - 1):
        print(nums_arr)
        curr_num = nums[i]
        next_num = nums[i + 1]
        diff = abs(curr_num - next_num)
        print(curr_num, next_num, diff)
        if diff > (nums_len - 1) or diff < 1:
            return False
        elif nums_arr[diff - 1] == False:
            nums_arr[diff - 1] = True
            i += 1
        else:
            return False
    if False in nums_arr:
        return False
    else:
        return True
    

print(jolly([1,2]))
print(jolly([1,2,4]))
print(jolly([1,2,4,7,11]))
print(jolly([-7,-5,-6]))
print(jolly([6,3,1,8,4,1,6,12]))
