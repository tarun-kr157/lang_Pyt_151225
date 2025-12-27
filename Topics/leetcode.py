arr = list(map(int, input("Enter the array elements separated by space(min size=2):\n").split()))
target = int(input("Enter the target value: "))
if len(arr) < 2:
    print("Invalid input!")
else:
    print("The input array is: ", arr)
    print("The target value is: ", target)
class Test():
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def twoSum(self):
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i, j]   
        
        


