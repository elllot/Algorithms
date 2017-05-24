import collections

# monotonic queue
def window_max(arr, k):
	if k == 1: return arr
	res = []
	window = collections.deque()
	for i in range(len(arr)):
		while window and window[0] < i - k + 1:
			window.popleft()
		while window and arr[window[-1]] < arr[i]:
			window.pop()
		window.append(i)
		if i >= k - 1:
			res.append(arr[window[0]])
	return res

def window_min(arr, k):
	if k == 1: return arr
	res = []
	window = collections.deque()
	for i in range(len(arr)):
		while window and window[0] < i - k + 1:
			window.popleft()
		while window and arr[window[-1]] > arr[i]:
			window.pop()
		window.append(i)
		if i >= k - 1:
			res.append(arr[window[0]])
	return res

if __name__ == "__main__":
	arr = [5,2,7,3,6,5]
	print(window_max(arr, 3))
	print(window_min(arr, 3))