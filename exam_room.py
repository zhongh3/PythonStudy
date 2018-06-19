class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        self.seated = []
        self.total_seats = N

    def seat(self):
        """
        :rtype: int
        """
        if len(self.seated) == self.total_seats:
            print("All seats are fully occupied.")
            return -1

        idx = self.find_seat()
        self.seated.append(idx)
        return idx

    def find_seat(self):
        """
        :rtype: int (index of the seat)
        """
        if not self.seated:
            return 0

        max_min = 0
        index = 0

        for i in range(self.total_seats):
            x = self.total_seats
            if i not in self.seated:
                for j in range(len(self.seated)):
                    temp = abs(i - self.seated[j])
                    # print("temp = {}".format(temp))
                    if temp < x:
                        x = temp
                    # print("x = {}".format(x))

                if max_min < x:
                    max_min = x
                    index = i
            # print("max_min = {}, index = {}".format(max_min, index))

        return index

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        if self.seated:
            try:
                self.seated.remove(p)
            except:
                print("Error removing p", p)
        # print("self.seated = {}".format(self.seated))

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)