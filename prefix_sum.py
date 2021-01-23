import math
arr=[2,6,4,9,3,8,7,5]

A=[]
for i in range(len(arr)):
	A.append([0,0,0])
	
k=0
for i in range(len(arr)-1,2*len(arr)-1):
	A.append([0,arr[k],0])
	k+=1
i=int(math.log(len(arr),2))
print(i)
for j in range(i):
	for k in range(len(arr)/pow(2,i+1)-1,len(arr)/pow(2,i)-1):
		A[i,1]=A[2*i+1,1]+A[2*i+2]
print(A)





