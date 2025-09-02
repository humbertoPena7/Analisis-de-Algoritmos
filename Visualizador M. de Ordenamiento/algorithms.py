def selectionSort(data, draw_callback):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw_callback(activos=[i, j, min_idx]); yield
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_callback(activos=[i, min_idx]); yield
    draw_callback(activos=[])

def bubbleSort(data, draw_callback):
    n = len(data)
    for i in range(n-1):
        for j in range(0, n-i-1):
            draw_callback(activos=[j, j+1]); yield
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        draw_callback(activos=[j, j+1]); yield
    draw_callback(activos=[])

 
def quick_sort(data, start=0, end=None):
    if end is None:
        end = len(data) - 1

    if start >= end:
        return

    pivot = data[start]
    left = start + 1
    right = end

    while True:
        while left <= right and data[right] >= pivot:
            right -= 1

        while left <= right and data[left] <= pivot:
            left += 1

        if left <= right:
            data[left], data[right] = data[right], data[left]
        else:
            break

    data[start], data[right] = data[right], data[start]

    quick_sort(data, start, right-1)
    quick_sort(data, right+1, end)


def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1


