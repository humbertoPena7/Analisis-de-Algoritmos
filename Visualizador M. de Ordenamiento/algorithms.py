def selectionSort(data, draw_callback):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw_callback(data, activos=[i, j, min_idx]); yield
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_callback(data, activos=[i, min_idx]); yield
    draw_callback(data, activos=[])

def bubbleSort(data, draw_callback):
    n = len(data)
    for i in range(n-1):
        for j in range(0, n-i-1):
            draw_callback(data, activos=[j, j+1]); yield
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        draw_callback(data, activos=[j, j+1]); yield
    draw_callback(data, activos=[])

def quickSort(data, draw_callback, start=0, end=None):
    if end is None:
        end = len(data) - 1

    if start >= end:
        return

    pivot = data[start]
    left = start + 1
    right = end

    draw_callback(data, activos=[start, left, right]); yield

    while True:
        while left <= right and data[right] >= pivot:
            right -= 1
            draw_callback(data, activos=[start, left, right]); yield

        while left <= right and data[left] <= pivot:
            left += 1
            draw_callback(data, activos=[start, left, right]); yield

        if left <= right:
            data[left], data[right] = data[right], data[left]
            draw_callback(data, activos=[start, left, right]); yield
        else:
            break

    data[start], data[right] = data[right], data[start]
    draw_callback(data, activos=[start, right]); yield

    yield from quickSort(data, draw_callback, start, right-1)
    yield from quickSort(data, draw_callback, right+1, end)

def mergeSort(data, draw_callback, start=0, end=None):
    if end is None:
        end = len(data) - 1

    if start >= end:
        return

    mid = (start + end) // 2

    # Dividir recursivamente
    yield from mergeSort(data, draw_callback, start, mid)
    yield from mergeSort(data, draw_callback, mid+1, end)

    # Combinar
    left = data[start:mid+1].copy()
    right = data[mid+1:end+1].copy()

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        draw_callback(data, activos=[k, start+i, mid+1+j]); yield
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        draw_callback(data, activos=[k, start+i]); yield
        data[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        draw_callback(data, activos=[k, mid+1+j]); yield
        data[k] = right[j]
        j += 1
        k += 1

    draw_callback(data, activos=list(range(start, end+1))); yield
