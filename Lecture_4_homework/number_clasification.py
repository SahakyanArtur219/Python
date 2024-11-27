def classify_numbers(numbers):
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    return even_numbers, odd_numbers





user_input = input("Enter a list of numbers separated by spaces, please fill with odd and even numbers: ")
numbers = list(map(int, user_input.split()))

even_numbers, odd_numbers = classify_numbers(numbers)

print("Even numbers is following:", even_numbers)
print("Odd numbers is following:", odd_numbers)