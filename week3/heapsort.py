def heapify(arr, n, i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if i!=largest:
        arr[i], arr[largest]=arr[largest], arr[i]
        heapify(arr, n, largest)
def ascending_order(arr):
    n=len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0]=arr[0], arr[i]
        heapify(arr, i, 0)

arr=[4, 5, 2 , 7, 8, 1, 2, 0]
ascending_order(arr)
print(arr)

