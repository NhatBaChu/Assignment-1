def remove_odd_numbers(numbers):

    result = []

    for n in numbers:
        if n % 2 == 0:
            result.append(n)

    return result


nums = [1,2,3,4,5,6,7,8]

new_list = remove_odd_numbers(nums)

print("Original:", nums)
print("Even only:", new_list)