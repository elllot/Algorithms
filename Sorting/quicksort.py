import random	

def quicksort(arr, start, end):
	if start < end:
		piv = random.randint(start, end) # randint is inclusive
		arr[piv], arr[end] = arr[end], arr[piv]
		lower = start
		for i in range(start, end):
			if arr[i] < arr[end]:
				arr[i], arr[lower] = arr[lower], arr[i]
				lower += 1
		arr[lower], arr[end] = arr[end], arr[lower]
		quicksort(arr, start, lower-1)
		quicksort(arr, lower+1, end)

def main(arr):
	quicksort(arr, 0, len(arr)-1)


if __name__ == '__main__':
	_size = 50
	arr = [random.randint(0, _size) for _ in range(_size)]
	print(arr)
	main(arr)
	print(arr)
