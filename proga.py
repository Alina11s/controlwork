# Примеры из задачи, раскомитить по очереди для выполнения
# arr = ["hello", "2", "world", ":-)"]
# arr = ["1234", "1567", "-2", "computer science"]
arr = ["Russia", "Denmark", "Kazan"]

def filter(arr):
    return [s for s in arr if len(s) <= 3]

filtered_arr = filter(arr)
print(filtered_arr)