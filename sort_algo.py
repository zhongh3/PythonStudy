# Implementation of different sorting algorithms


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


def main():
    inputs = [3, 2, 5, 1, 9]
    print("Before Sorting: {}".format(inputs))

    # select_sort(inputs)
    # print("After Selection Sort: {}".format(inputs))

    merge_sort(inputs)
    print("After Merge Sort: {}".format(inputs))


if __name__ == "__main__":
    main()


