def matrix_sum(matrix1, matrix2):
    sum = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            suma = int(matrix2[i][j]) + int(matrix1[i][j])
            row.append(suma)
        sum.append(row)
    return sum
x=0
y=0


matrix1 = []
matrix2 = []
loop1= 0
loop2=0
while x == 0:
    list = []
    list = str(input()).split(" ")
    if list[0] == "":
        x = 1
        break
    matrix1.append(list)
while y == 0:
    list = []
    list = str(input()).split(" ")
    if list[0]=="":
        y = 1
        break
    matrix2.append(list)
if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
    print("Not the same size")
else:
    print(matrix_sum(matrix1, matrix2))
