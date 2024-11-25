import random

class Matrix:
    
    n = int(input("Enter number of rows: "))
    m = int(input("Enter number of cols: "))
    
    def __init__(self):
        self.matrix = [] 
        
        for i in range(Matrix.n):
            row = []
            for i in range(Matrix.m):
                row.append(random.randint(1, 50))
            self.matrix.append(row)
            
    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(f"{num:>{3}}" for num in row))
            
    def mean(self):
        mean = 0
        for i in range(Matrix.n):
            for j in range(Matrix.m):
                mean += self.matrix[i][j]
                
        mean = mean / (Matrix.n * Matrix.m)
        
        return mean
    
    def sum_of_row(self, row):
        sum_row = 0
        for i in self.matrix[row]:
            sum_row += i
            
        return sum_row
    
    def average_of_column(self, col):
        average_col = 0
        for row in self.matrix:
            average_col += row[col]
        
        average_col = average_col / Matrix.n   
        
        return average_col    
    
    def get_submatrix(self, col1, col2, row1, row2):        
        submatrix = []
        for i in range(row1, row2 + 1):
            submatrix.append(self.matrix[i][col1:col2 + 1])
        
        return submatrix     
                     
matrix = Matrix()
matrix.print_matrix()
print(f"Mean of the matrix -> {matrix.mean()}")
print(f"Sum of a given row -> {matrix.sum_of_row(2)}")
print(f"Average of a given column -> {matrix.average_of_column(1)}")
submatrix = matrix.get_submatrix(1, 2, 1, 2)
print("Submatrix")
for row in submatrix:
    print(" ".join(f"{num:>{3}}" for num in row))