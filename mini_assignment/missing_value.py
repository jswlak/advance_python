#Problem - we hava a list of n-1 numbers from 1 to n, we have to find missing numbers.



def find_missing(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2      
    return total - sum(nums)      


#testing ------


nm = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 

print(nm)


print(find_missing(nm)) #output = 11

