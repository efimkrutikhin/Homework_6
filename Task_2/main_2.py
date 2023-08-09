import random

def find_indices_in_range(arr, min_val, max_val):
    indices = []
    for i, num in enumerate(arr):
        if min_val <= num <= max_val:
            indices.append(i)
    return indices

def main():
    input_list = [1, 5, 88, 100, 2, -4]  # Здесь можно задать список случайных чисел
    min_val = float(input("Введите минимальное значение: "))
    max_val = float(input("Введите максимальное значение: "))
    
    indices = find_indices_in_range(input_list, min_val, max_val)
    
    print("Индексы элементов в заданном диапазоне:", indices)

if __name__ == "__main__":
    main()
