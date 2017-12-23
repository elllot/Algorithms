import random

def msort(arr, low, high):
    if low < high:
        mid = low + (high - low) // 2
        piv = mid + 1
        msort(arr, low, mid)
        msort(arr, piv, high)
        bot = arr[low:piv]
        top = arr[piv:high+1]
        b = t = 0
        pos = low
        while b < len(bot) and t < len(top):
            if bot[b] < top[t]:
                arr[pos] = bot[b]
                b += 1
            else:
                arr[pos] = top[t]
                t += 1
            pos += 1
        arr[pos:high+1] = bot[b:] if b < len(bot) else top[t:]

def mergesort(arr):
    msort(arr, 0, len(arr)-1)

if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(50)]
    print(arr)
    mergesort(arr)
    print(arr)