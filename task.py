import random


def generate_array(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]


def print_array(arr):
    items = [f"[cell - {i},value - {v}]" for i, v in enumerate(arr)]
    print("{" + ",".join(items) + "}")


def need_swap(a, b, ascending):
    return a > b if ascending else a < b


def bubble_sort(arr, ascending):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if need_swap(arr[j], arr[j + 1], ascending):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr, ascending):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and need_swap(arr[j], key, ascending):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr, ascending):
    n = len(arr)
    for i in range(n - 1):
        best = i
        for j in range(i + 1, n):
            if need_swap(arr[best], arr[j], ascending):
                best = j
        arr[i], arr[best] = arr[best], arr[i]


def main():
    original = generate_array(10, -20, 50)

    print("Початковий масив:")
    print_array(original)

    algorithms = [
        ("Bubble sort", bubble_sort),
        ("Insertion sort", insertion_sort),
        ("Selection sort", selection_sort),
    ]

    for name, sort_func in algorithms:
        print()
        for ascending in (True, False):
            arr = original.copy()
            sort_func(arr, ascending)
            order = "за зростанням" if ascending else "за спаданням"
            print(f"{name} ({order}):")
            print_array(arr)


if __name__ == "__main__":
    main()