from my_project.main import bubbleSort, selectionSort, mergeSort, insertionSort

preSortedList = [1, 2, 3, 4, 5]
reversedList = [5, 4, 3, 2, 1]
jumbledList = [1, 3, 2, 5, 4]
correctSortedOrder = [1, 2, 3, 4, 5]


def test_bubble_sort():
    assert bubbleSort(preSortedList) == correctSortedOrder
    assert bubbleSort(reversedList) == correctSortedOrder
    assert bubbleSort(jumbledList) == correctSortedOrder


def test_selection_sort():
    assert selectionSort(preSortedList) == correctSortedOrder
    assert selectionSort(reversedList) == correctSortedOrder
    assert selectionSort(jumbledList) == correctSortedOrder


def test_merge_sort():
    assert mergeSort(preSortedList) == correctSortedOrder
    assert mergeSort(reversedList) == correctSortedOrder
    assert mergeSort(jumbledList) == correctSortedOrder


def test_insertion_sort():
    assert insertionSort(preSortedList) == correctSortedOrder
    assert insertionSort(reversedList) == correctSortedOrder
    assert insertionSort(jumbledList) == correctSortedOrder
