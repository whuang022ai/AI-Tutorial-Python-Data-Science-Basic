

def get_Inputs(size):
	num = [None]*size
	print('Please input the numbers to sort')
	for i in range(size):
		num[i]=int(input())
	return num
	
	
def bubble_sort(arr,size):
	for i in range(size):
		j = i+1
		for j in range(size):
			if( arr[i]<arr[j] ):
				tmp=arr[i]
				arr[i]=arr[j]
				arr[j]=tmp
	return arr
	
input=get_Inputs(6)
sorted=bubble_sort(input,6)
print(sorted)