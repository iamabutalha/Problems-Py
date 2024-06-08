



def checkMin(arr1,arr2):
    """Function to check min value array in two arrays"""
    arr1Count = 0
    arr2Count = 0

    for i in range(len(arr1)):
        arr1Count += 1
    
    for i in range(len(arr2)):
        arr2Count += 1
    
    
    if arr1Count > arr2Count:
        return arr2Count
    elif arr2Count > arr1Count:
        return arr1Count
    else:
        return arr1Count
    
    return 0

# print(checkMin([1,2,3,4],[1,2,3,4,5]))
# print(checkMin([2],[2,3,43,3]))

def checkPattern(arr1,arr2):
    """A Function that check if the first digit is 3 and the last digit is 1 return true and false other wise"""
    # length = checkMin(arr1,arr2)
    # print(length)
    # print(checkMin(arr1,arr2))
    for i in range(0,checkMin(arr1,arr2)):
        if arr1[0] == 3 and arr2[0] == 3 and arr1[len(arr1)-1] == 1 and \
        arr2[len(arr2) - 1] == 1:
            return True
            
    return False


print(checkPattern([1,2,3],[1,2,3])) #→ False
print(checkPattern([9,2,3,4],[2,3,4])) #→ False
print(checkPattern([0,2,4,3],[0,1,4,3])) #→ False
print(checkPattern([3,2,4,1],[3,1,4,1])) #→ True
print(checkPattern([3,2,3,1],[3,3,1])) #→ True
print(checkPattern([3,1],[3,3,1])) #→ True
print(checkPattern([1,2,3,1],[3,3,1])) #→ False
print(checkPattern([3,2,3,4,5,1],[3,1])) #→ True
print(checkPattern([],[3,3,1])) #→ False
print(checkPattern([3],[3])) #→ False
print(checkPattern([3,2,5,9,8,0,1],[3,4,6,7,0,86,5,4,3,1])) #→ True
