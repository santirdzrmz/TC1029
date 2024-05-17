def matrix_creator(rows, columns):
    matrix = []
    while len(matrix) < rows:
        row = []
        while len(row) < columns:
            number = int(input())
            row.append(number)
        matrix.append(row)
    return matrix 

def matrix_sum(matrix):
    sum = []
    c = 0
    while c < len(matrix[0]):
        total = 0
        r=0
        while r <  len(matrix):
            total = total + matrix[r][c]
            r = r+1
        sum.append(total)
        c= c+1
    return sum
def main():
    print("Input the value of rows in the matrix: ")
    rows = int(input())
    print("Input the value of columns in the matrix")
    columns = int(input())
    if columns == 0 or rows == 0:
        print("Error")
    else:
        matrix = matrix_creator(rows, columns)
        sum = matrix_sum(matrix)
        print(sum)

main()