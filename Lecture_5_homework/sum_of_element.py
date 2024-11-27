def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        numbers = [num for num in numbers if num >= 0]
    return sum(numbers)

user_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = list(map(float, user_input.split()))  

exclude_neg = input("Do you want to exclude the negative numbers? write \"yes\" or \"no\": ").strip().lower()
exclude_negative = (exclude_neg == "yes") 

result = sum_of_elements(numbers_list, exclude_negative=exclude_negative)
print(f"Based on your choosing case the sum of the elements is: {result}")
