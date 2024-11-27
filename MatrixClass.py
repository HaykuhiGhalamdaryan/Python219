import random

class Matrix:
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(random.randint(1, 20))
            self.matrix.append(row)
            
    def __str__(self):
        result = []
        for row in self.matrix:
            result.append(" ".join(f"{num:>{3}}" for num in row))
        return "\n".join(result)

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = Matrix(self.rows, self.cols)
        result.matrix = []
        for i in range(self.rows):
            row = [self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]
            result.matrix.append(row)
        
        return result
    
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        result = Matrix(self.rows, self.cols)
        result.matrix = []
        for i in range(self.rows):
            row = [self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)]
            result.matrix.append(row)

        return result
    
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication.")
        
        result = Matrix(self.rows, other.cols)
        result.matrix = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                new_elem = 0
                for k in range(self.cols):
                    new_elem += self.matrix[i][k] * other.matrix[k][j]
                row.append(new_elem)
            result.matrix.append(row)
            
        return result
           
matrix1 = Matrix(3, 3)
matrix2 = Matrix(3, 3)
print("Matrix1")
print(matrix1)
print("\nMatrix2")
print(matrix2)
print("\nAddition of matrices")
print(matrix1 + matrix2)
print("\nSubtraction of matrices")
print(matrix1 - matrix2)
print("\nMultiplication of matrices")
print(matrix1 * matrix2)