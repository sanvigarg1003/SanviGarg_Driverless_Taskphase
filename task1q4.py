#formulatask1q4
m=int(input("Enter number of rows of matrix A"))
n=int(input("Enter number of columns of matrix A"))
p=int(input("Enter number of rows of matrix B"))
q=int(input("Enter number of columns in matrix B"))
#for matrix multiplication to work the number of columns of first matrix needs to be equal to the number of rows of the second matrix
if n!=p:
            print("ERROR")
else:
            A=[]
            B=[]
            print("Enter first matrix")
            for i in range(m):
                row=list(map(int,input().split()))
                A.append(row)
            print("Enter second matrix")
            for i in range(p):
                         row=list(map(int, input().split()))
                         B.append(row)
                     
                            
            result=[[0 for j in range(q)]for i in range (m)]
            for i in range(m):
                    for j in range(q):
                        for k in range(n):
                            result[i][j]=result[i][j]+A[i][k]*B[k][j]
            print("The resulting matrix is")
            for row in result:
                 print(row)
