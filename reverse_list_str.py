def rev_list(lst):

    if not lst:  # equivalent to lst == []
        return []

    rest_rev = rev_list(lst[1:])
    first = lst[0:1]  # slicing returns a new list

    return rest_rev + first


def rev_list2(lst):

    def rev_list_helper(index):
        if index == -1:
            return []

        rest_rev = rev_list_helper(index-1)
        first = [lst[index]]

        return first + rest_rev

    return rev_list_helper(len(lst)-1)


def rev_list3(lst):

    def rev_list_helper3(index):
        if index == len(lst):
            return []

        rest_rev = rev_list_helper3(index+1)
        first = [lst[index]]

        return rest_rev + first

    return rev_list_helper3(0)


def rev_str(s):
    if not s:  # equivalent to s == ""
        return s

    rest_rev = rev_str(s[1:])
    first = s[0:1]

    return rest_rev + first


def reverse(seq):
    seq_type = type(seq)
    empty_seq = seq_type()

    if seq == empty_seq:
        return empty_seq

    rest_rev = reverse(seq[1:])
    first = seq[0:1]

    return rest_rev + first


def main():
    print(rev_list([1, 2, 3, 4]))
    print(rev_list2([1, 2, 3, 4]))
    print(rev_list3([1, 2, 3, 4, 5, 6]))
    print(rev_str("Hello"))

    print(reverse("HelloWorld"))
    print(reverse([1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    main()
