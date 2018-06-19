import datetime
import random
import time


def main():
    file = open("ListAccessTiming.xml", "w")

    file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
    file.write('<Plot title="Average List Element Access Time">\n')

    xmin = 1000
    xmax = 200000

    x_list = []  # list size
    y_list = []  # average access time for 1000 retrievals

    for x in range(xmin, xmax+1, 1000):
        x_list.append(x)
        prod = 0
        lst = [0]*x  # a list of size x with all 0's
        time.sleep(1)   # let any garbage collection complete or at least settle down

        start_time = datetime.datetime.now()

        for v in range(1000):
            index = random.randint(0, x-1)
            val = lst[index]
            prod = prod * val

        end_time = datetime.datetime.now()

        delta_t = end_time - start_time

        access_time = delta_t.total_seconds()*1000  # divide by 1000 and convert to microseconds(*1e-6)

        y_list.append(access_time)

    file.write('   <Axes>\n')
    file.write('     <XAxis min="' + str(xmin) + '" max="' + str(xmax) + '">List Size</XAxis>\n')
    file.write('     <YAxis min="' + str(min(y_list)) + '" max="' + str(60) + '">Microseconds</YAxis>\n')
    file.write('   </Axes>\n')

    file.write('   <Sequence title="Average Access Time vs List Size" color="red">\n')

    for i in range(len(x_list)):
        file.write('     <DataPoint x="' + str(x_list[i]) + '" y="' + str(y_list[i]) + '"/>\n')

    file.write('   </Sequence>\n')

    x_list = lst
    y_list = [0] * 200000

    time.sleep(2)

    for i in range(100):
        start_time = datetime.datetime.now()
        index = random.randint(0, 200000-1)
        x_list[index] = x_list[index] + 1
        end_time = datetime.datetime.now()
        delta_t = end_time - start_time
        y_list[index] = y_list[index] + delta_t.total_seconds()*1000000

    file.write('   <Sequence title="Access Time Distribution" color="blue">\n')

    for i in range(len(x_list)):
        if x_list[i] > 0:
            file.write('     <DataPoint x="' + str(i) + '" y="' + str(y_list[i]/x_list[i]) + '" />\n')

    file.write('   </Sequence>\n')
    file.write('</Plot>\n')

    file.close()
    print("Execution is completed.")


if __name__ == "__main__":
    main()
