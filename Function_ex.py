#[1,2,3] is in the [1,11,2,1,2,3,4]
array = [1,1,2,4,1,2,3]
length = len(array)
def arraycheck(nums):
        i = nums.index(1)
        while(i != length):
            j = i +2
            if(j  <= length):
                if(nums[i] == 1 and  nums[i+1] == 2 and nums[i+2] == 3):
                    return True
                    break
            i+=1
        return False

print(arraycheck(array))
