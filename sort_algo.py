# Implementation of different sorting algorithms


#######################################
# 1. Selection Sort
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


def main():
    inputs = [3, 2, 5, 1, 9]
    print("Before Sorting: {}".format(inputs))

    select_sort(inputs)
    print("After Selection Sort: {}".format(inputs))


if __name__ == "__main__":
    main()


