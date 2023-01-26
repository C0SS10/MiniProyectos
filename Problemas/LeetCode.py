#   Sumar la lista (Running Sum)
def runningSum(nums):
    #   [0+1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5]
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
    return nums

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    print(runningSum(nums))