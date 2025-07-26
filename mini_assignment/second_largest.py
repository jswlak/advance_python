#Our Goal is to find the 2nd largest number from list


def second_largest(nums):
    nums = list(set(nums))  # Remove duplicates
    nums = sorted(nums)
    length = len(nums)

    if length >=2:

        #index of second largest is lenght -2:

        idx_second_largest = length -2

        print(nums[idx_second_largest])
    else:
        None


# testing -------------------------

number = [16, 19, 34, 56, 49]


second_largest(number)

#output - 49


nm = [5,6]
second_largest(nm)