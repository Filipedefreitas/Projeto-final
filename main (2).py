import time
import random

# Criar uma lista de 10.000 valores aleatórios
random_values = [random.randint(1, 100000) for _ in range(10000)]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if not current_node.left:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if not current_node.right:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if not current_node or current_node.value == value:
            return current_node
        if value < current_node.value:
            return self._search_recursive(current_node.left, value)
        return self._search_recursive(current_node.right, value)

# Valor aleatório para busca
target = random_values[5000]

# Teste de tempo para busca linear
start_time = time.time()
result_linear = linear_search(random_values, target)
end_time = time.time()
time_taken_linear = end_time - start_time
print(f"Tempo de busca linear: {time_taken_linear} segundos")

# Teste de tempo para busca binária
sorted_random_values = sorted(random_values)
start_time = time.time()
result_binary = binary_search(sorted_random_values, target)
end_time = time.time()
time_taken_binary = end_time - start_time
print(f"Tempo de busca binária: {time_taken_binary} segundos")

# Teste de tempo para busca em BST
bst = BST()
for value in random_values:
    bst.insert(value)
start_time = time.time()
result_bst = bst.search(target)
end_time = time.time()
time_taken_bst = end_time - start_time
print(f"Tempo de busca em BST: {time_taken_bst} segundos")
