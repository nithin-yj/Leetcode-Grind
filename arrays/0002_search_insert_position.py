#Leetcode - 35
'''
My approach:
    see here the question says sorted array , it is very obvious that our first though
    id to use binary search , as its time
    complexity is log(n) , but 
    -> we could also try with the linear search way ,
    -> so as usual we traverse the array and try to find the elements that are equal to or greater than target element
    -> if don't gete any element , then it very obvious that the target belongs to be at the end of the aray
    -> so we return the length of the array 

    Time Complexity : o(n)
    Space Complexity : o(1)

    might add new method later
'''
#Code: 
def select_at_insert_position(nums,target):
    for i in range(len(nums)):
        if nums[i]>=target:
            return i

    return len(nums)



if __name__=='__main__':
    nums = [1,3,5,6]
    target = 5
    res=select_at_insert_position(nums,target)
    print(res) #2

