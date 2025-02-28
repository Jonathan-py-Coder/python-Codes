list=([1,2,3],[4,5,6],[7,8,9])
print(list)

rows=len(list)
colums=len(list[0])
print("Rows: ",rows)
print("Colums: ",colums)

print(list[1][1])

for i in range(0,rows):
    for j in range(0,colums):
        print(list[i][j],end="")
    print("\n")

rows=int(input("Enter the numeber of rows-"))
colums=int(input("Enter the number of colums-"))
matrix=[]

for i in range(rows):
    temp=[]
    for j in range(colums):
        x=int(input("Enter your element-"))
        temp.append(x)
    matrix.append(temp)

for a in range(rows):
    for b in range(colums):
        print(matrix[a][b],end=" ")
    print("\n")

rc=int(input("Enter the diamention of the matrix"))

for i in range(n):
    temp=[]
    for j in range(n):
        x=int(input("enter your number"))
        temp.append(x)
    matrix.append(temp)

for i in range(n):
    print(matix[i][j])