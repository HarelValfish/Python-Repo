# def numlist(numbers):
#     total_sum = sum(numbers)
#     count = len(numbers)
#     average = total_sum / count if count > 0 else 0
#     return (total_sum, count, average)

# print(numlist([10, 20, 30]))    

# #==========================

# def find_min_max(numbers):
#     if not numbers:
#         return

#     smallest = min(numbers)
#     largest = max(numbers)
#     return (smallest, largest)

# print(find_min_max([5, 2, 6, 9]))

# #==========================
# def is_even(num):
#     return num % 2 ==0

# def filter_and_sort(numbers):
#     filtered_iterator = filter(is_even, numbers)
#     return sorted(list(filtered_iterator))

# print(filter_and_sort([7, 2, 8, 10, 5]))

# def odd_even(x):
#     if x % 2 == 0:
#         print(f"{x} is an even number.")
#     else:
#         print(f"{x} is an odd number.")
        
# odd_even(2)
    
# def checkgrade():
#     grade = int(input("Enter your grade: "))
#     if grade >= 60:
#         print(grade)
#     else:
#         return
    
# checkgrade()

#=============================

# def checklist(nums):
#     total = sum(nums)
#     count = len(nums)
#     avg = total / count
#     if nums == []:
#         print("None")
#     else:
#         print(f"the average is {avg}")
        
# checklist([1, 6, 3, 9, 12])

#===============================
# def is_greater(num, threshold):
#     return num > threshold

# def checklarger(numbers, threshold=10):
#     result = filter(lambda x: x > threshold, numbers)
    
# checklarger(10, ([3, 6, 9, 11, 20]))

