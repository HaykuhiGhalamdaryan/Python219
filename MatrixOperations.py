import random

def generate_random_matrix(rows, cols):
    
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(1, 100))  
        matrix.append(row)
        
    return matrix
    
def get_column_sum(matrix, col_index):
    
    column_sum = 0
    for row in matrix:
        column_sum += row[col_index]
        
    return column_sum

def get_row_average(matrix, row_index):
    
    row_sum = 0
    for num in matrix[row_index]:
        row_sum += num
        
    row_average = row_sum / len(matrix[row_index])
    
    return row_average

matrix = generate_random_matrix(3, 4)
for row in matrix:
    print(" ".join(f"{num:>{3}}" for num in row))
    
column_sum = get_column_sum(matrix, 2)
print("The sum of all values ​in the specified column:", column_sum)   
    
row_average = get_row_average(matrix, 1)
print("The average of all values ​in the specified row:", row_average)