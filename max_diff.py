

def maxIndexDiff(arr,n):
	Lmin = []
	Rmax = []

	for i in range(n):
		Lmin.append(0)
		Rmax.append(0)

	Lmin[0] = arr[0]
	for i in range(1,n):
		Lmin[i] = min(arr[i],Lmin[i-1])

	Rmax[n-1] = arr[n-1]
	for j in range(n-2,-1,-1):
		Rmax[j] = max(arr[j],Rmax[j+1])


	i = 0
	j = 0
	maxdiff = -1
	while(j<n and i<n):
		if(Lmin[i] <= Rmax[j]):
			maxdiff = max(maxdiff,j-i)
			j = j+1
		else:
			i = i+1

	return maxdiff


print(maxIndexDiff([25,7,34,8,43,2,4,5,6,7,8,9,0,43,2,5,2,12,1,0],20))
