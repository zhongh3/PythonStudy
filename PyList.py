class PyList:
    def __init__(self, content=[], size=10):
        self.items = [None] * size
        self.num_items = 0  # number of locations in the internal list that's being used
        self.size = size  # size of internal list

        for e in content:
            self.append(e)

    def __getitem__(self, index):
        if 0 <= index < self.num_items:
            return self.items[index]

        raise IndexError("PyList index out of range.")

    def __setitem__(self, index, value):
        if 0 <= index < self.num_items:
            self.items[index] = value
            return

        raise IndexError("PyList assignment index out of range.")

    def __add__(self, other):
        result = PyList(size=self.num_items+other.num_items)

        for i in range(self.num_items):
            result.append(self.items[i])

        for i in range(other.num_items):
            result.append(other.items[i])

        return result

    # The method is hidden since it starts with two underscores.
    # It's only available to the class.
    def __make_room(self):
        # increase list size by 1/4, add 1 for handle the case when self.size = 0
        new_length = (self.size // 4) + self.size + 1
        new_list = [None] * new_length
        for i in range(self.num_items):
            new_list[i] = self.items[i]

        self.items = new_list
        self.size = new_length

    def append(self, item):
        if self.num_items == self.size:
            self.__make_room()

        self.items[self.num_items] = item
        self.num_items += 1

    def insert(self, index, item):
        if self.num_items == self.size:
            self.__make_room()

        if index < self.num_items:
            for i in range(self.num_items-1, index-1, -1):
                self.items[i+1] = self.items[i]

            self.items[index] = item
            self.num_items += 1
        else:
            self.append(item)

    def __delitem__(self, index):
        for i in range(index, self.num_items-1):
            self.items[i] = self.items[i+1]

        self.num_items -= 1

    def __eq__(self, other):
        if type(other) != type(self):
            return False

        if other.num_items != self.num_items:
            return False

        for i in range(self.num_items):
            if self.items[i] != other.items[i]:
                return False

        return True

    def __iter__(self):
        for i in range(self.num_items):
            yield self.items[i]

    def __len__(self):
        return self.num_items

    def __contains__(self, item):
        for i in range(self.num_items):
            if self.items[i] == item:
                return True

        return False

    def __str__(self):
        s = "["
        for i in range(self.num_items):
            s = s + repr(self.items[i])
            if i < self.num_items-1:
                s = s + ", "
        s = s + "]"
        return s

    def __repr__(self):
        s = "PyList(["
        for i in range(self.num_items):
            s = s + repr(self.items[i])
        if i < self.num_items-1:
            s = s + ", "
        s = s + "])"
        return s
