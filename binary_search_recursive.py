#Find data in list using recursive binary seach



data = [1,2,3,4,5,6,7,8,9,10,13,15,72,89,105]
target = 15


def binary_search_recursive(data, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return True 
		elif target < data [mid]:
			return binary_search_recursive(data, target, low, mid -1)
		else:
			return binary_search_recursive(data, target, mid+1, high)

print(binary_search_recursive(data, target, 0, len(data) - 1))