def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            return iterations, arr[mid]

    return iterations, upper_bound

sorted_array = [0.1, 0.5, 1.2, 3.5, 5.7, 7.8, 9.0]
target_value = 6.8

print(binary_search(sorted_array, target_value))
