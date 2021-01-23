def kthSmallestElement(arr,l,r,k):


	if k<0 or k>r-l+1:
		return -9999999999
	#print("a")

	i=0
	median=[]

	n=r-l+1


	while i<=(n//5) and n>=5:

		arr[l+i*5:l+i*5+5]=sorted(arr[l+i*5:l+i*5+5])
		median.append(l+i*5+2)

		i+=1
	if i==0:
		pivot=arr[l]
	elif i==1:
		pivot=median[0]
	else:
		pivot=kthSmallestElement(median,0,i-1,i//2)

	pos=partition(arr,l,r,pivot)

	if (pos - l == k - 1):  
            return arr[pos]  
	if (pos - l > k - 1):  
		return kthSmallestElement(arr, l, pos - 1, k)  
	return kthSmallestElement(arr, pos + 1, r, k - pos + l - 1)  

def partition(arr, l, r, x): 
	for i in range(l, r): 
		if arr[i] == x: 
			arr[i],arr[r]=arr[r],arr[i]
			break
  
	x = arr[r]  
	i = l  
	for j in range(l, r):  
		if (arr[j] <= x):  
			arr[i],arr[j]=arr[j],arr[i]
			i += 1
	arr[i],arr[r]=arr[r],arr[i]
	return i 

arr=[9,8,7,6,5,4,3,2,1,0]
print(kthSmallestElement(arr,0,len(arr)-1,4))

