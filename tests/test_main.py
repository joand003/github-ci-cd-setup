import my_project.main as sorts

listOne = [1, 2, 3, 4, 5]
listTwo = [5, 4, 3, 2, 1]
listThree = [1, 3, 2, 5, 4]
sortedList = [1, 2, 3, 4, 5]


def test_bubble_sort():
    assert sorts.bubbleSort(listOne) == sortedList
    assert sorts.bubbleSort(listTwo) == sortedList
    assert sorts.bubbleSort(listThree) == sortedList


def test_selection_sort():
    assert sorts.selectionSort(listOne) == sortedList
    assert sorts.selectionSort(listTwo) == sortedList
    assert sorts.selectionSort(listThree) == sortedList


def test_merge_sort():
    assert sorts.mergeSort(listOne) == sortedList
    assert sorts.mergeSort(listTwo) == sortedList
    assert sorts.mergeSort(listThree) == sortedList


def test_insertion_sort():
    assert sorts.insertionSort(listOne) == sortedList
    assert sorts.insertionSort(listTwo) == sortedList
    assert sorts.insertionSort(listThree) == sortedList
