
def SelectionSort(arr):
 count = 0
 for i in range(len(arr)):
    min = i
    for j in range(i+1, len(arr)):
      count+=1
      if arr[min] > arr[j]:
       min = j
    arr[i], arr[min] = arr[min], arr[i]
 print("Evaluation", count)
 return arr


arr=[1,5,3,2,0,8]

print(SelectionSort(arr))