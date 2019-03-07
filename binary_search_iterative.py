#Find data in list using iterative binary seach

data = [1,2,3,4,5,6,7,8,9,10,13,15,72,89,105]
target = 124

def binary_search_iterative(data,target):
	low = 0 
	high = len(data) - 1

	while low <= high:
		mid = (low + high) // 2
		if target == data[mid]:
			return True 
		elif target < data[mid]:
			high = mid - 1 
		else: 
			low = mid + 1
	return False

a = binary_search_iterative(data, target)
print(a)