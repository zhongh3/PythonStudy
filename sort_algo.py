# Implementation of different sorting algorithms
import random


#######################################
# 1. Selection Sort - O(n^2)
#######################################
def select_sort(seq):
    def select(seq, start):
        min_idx = start

        for i in range(start+1, len(seq)):
            if seq[i] < seq[min_idx]:
                min_idx = i

        return min_idx

    for i in range(len(seq)-1):
        min_idx = select(seq, i)

        tmp = seq[i]
        seq[i] = seq[min_idx]
        seq[min_idx] = tmp


#######################################
# 2. Merge Sort - O(nlogn)
#######################################
# divide and conquer -- recursive (usually)
def merge_sort(seq):
    def merge_sort_recursive(seq, start, stop):
        if start >= (stop - 1):
            return

        mid = (start + stop) // 2
        merge_sort_recursive(seq, start, mid)
        merge_sort_recursive(seq, mid, stop)
        merge(seq, start, mid, stop)

    def merge(seq, start, mid, stop):
        lst = []
        i = start
        j = mid

        while i < mid and j < stop:
            if seq[i] < seq[j]:
                lst.append(seq[i])
                i += 1
            else:
                lst.append(seq[j])
                j += 1

        while i < mid:
            lst.append(seq[i])
            i += 1

        # copy the elements back to the original sequence
        # the elements from index j to the end are untouched
        for i in range(len(lst)):
            seq[start+i] = lst[i]

    merge_sort_recursive(seq, 0, len(seq))


#######################################
# 3. Quicksort - O(nlogn)
#######################################
# divide and conquer -- recursive (usually)
def quicksort(seq):
    def partition(seq, start, stop):
        pivot_idx = start
        pivot = seq[pivot_idx]
        i = start + 1
        j = stop - 1

        while i <= j:
            while i <= j and seq[i] <=  pivot:
                i += 1
            while i <= j and pivot < seq[j]:
                j -= 1

            # swap
            if i < j:
                tmp = seq[i]
                seq[i] = seq[j]
                seq[j] = tmp
                i += 1
                j -= 1

        seq[pivot_idx] = seq[j]
        seq[j] = pivot

        return j

    def quicksort_recursive(seq, start, stop):
        if start >= stop - 1:  # empty sequence: start > stop - 1; others: start == stop - 1
            return

        pivot_idx = partition(seq, start, stop)

        quicksort_recursive(seq, start, pivot_idx)
        quicksort_recursive(seq, pivot_idx + 1, stop)

    # randomize the sequence to guarantee a random choice of the pivot
    random.shuffle(seq)

    print("After Randomization: {}".format(seq))

    quicksort_recursive(seq, 0, len(seq))


def main():
    random.seed(1)
    inputs = random.sample(range(10), 10)
    # inputs = [1, 2, 3, 4, 5]
    print("Before Sorting: {}".format(inputs))

    # select_sort(inputs)
    # print("After Selection Sort: {}".format(inputs))

    # merge_sort(inputs)
    # print("After Merge Sort: {}".format(inputs))

    quicksort(inputs)
    print("After Quicksort: {}".format(inputs))


if __name__ == "__main__":
    main()


