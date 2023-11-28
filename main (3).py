import random
import time

# Gerar uma lista de 10.000 valores aleatórios
random_values = [random.randint(1, 100000) for _ in range(10000)]

def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
      for j in range(0, n-i-1):
          if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr):
  if len(arr) > 1:
      mid = len(arr) // 2
      left_half = arr[:mid]
      right_half = arr[mid:]

      merge_sort(left_half)
      merge_sort(right_half)

      i = j = k = 0

      while i < len(left_half) and j < len(right_half):
          if left_half[i] < right_half[j]:
              arr[k] = left_half[i]
              i += 1
          else:
              arr[k] = right_half[j]
              j += 1
          k += 1

      while i < len(left_half):
          arr[k] = left_half[i]
          i += 1
          k += 1

      while j < len(right_half):
          arr[k] = right_half[j]
          j += 1
          k += 1

def quick_sort(arr):
  if len(arr) <= 1:
      return arr
  else:
      pivot = arr[0]
      less_than_pivot = [x for x in arr[1:] if x <= pivot]
      greater_than_pivot = [x for x in arr[1:] if x > pivot]
      return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def linear_search(arr, target):
   for i in range(len(arr)):
    if arr[i] == target:
        return i
    return -1

# Teste de tempo para Bubble Sort
values_bubble = random_values.copy()
start_time = time.time()
bubble_sort(values_bubble)
end_time = time.time()
time_taken_bubble = end_time - start_time
print(f"Tempo de execução do Bubble Sort: {time_taken_bubble} segundos")

# Teste de tempo para Merge Sort
values_merge = random_values.copy()
start_time = time.time()
merge_sort(values_merge)
end_time = time.time()
time_taken_merge = end_time - start_time
print(f"Tempo de execução do Merge Sort: {time_taken_merge} segundos")

# Teste de tempo para Quick Sort
values_quick = random_values.copy()
start_time = time.time()
quick_sort(values_quick)
end_time = time.time()
time_taken_quick = end_time - start_time
print(f"Tempo de execução do Quick Sort: {time_taken_quick} segundos")


