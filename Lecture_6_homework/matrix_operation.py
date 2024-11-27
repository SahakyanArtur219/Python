import random

def generate_random_matrix(rows, cols):
    return [[random.randint(1, 100) for i in range(cols)] for j in range(rows)]


def get_column_sum(matrix, column_index):
    sum = 0
    for row in matrix:
         sum+=row[column_index]
    return sum


def get_row_average(matrix, row_index):
    return sum(matrix[row_index]) / len(matrix[row_index])


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = generate_random_matrix(rows, cols)
print("Generated Matrix:")
for row in matrix:
    print(row)


column_index = int(input(f"Enter column index (0 to {cols - 1}) to sum: "))

try:
    print(f"Sum of column {column_index}: {get_column_sum(matrix, column_index)}")
    t = True
except Exception as e:
    print("The number you entered is out of matrix range")

row_index = int(input(f"Enter row index (0 to {rows - 1}) to average: "))

try:  
    print(f"Average of row {row_index}: {get_row_average(matrix, row_index)}")
    t = True
except Exception as e:
        print("The number you entered is out of matrix range")