import ast

debugging = True


def process_input():
    # filename = input("please enter input filename: ")
    filename = "./webpage.html"

    file = open(filename, mode="r", encoding='UTF-8')

    data = file.readline().strip()

    start = data.find("<script>window.__INITIAL_STATE__=")
    if start != -1:
        start2 = data.find('"pages":[', start) + len('"pages":[')
        if start2 != -1:
            end = data.find("]", start2)
            cut = data[start2:end]  # cut: string

            if debugging:
                log_file = open("cut.html", mode='w', encoding='UTF-8')
                log_file.write(cut)
                log_file.close()

            items = ast.literal_eval(cut)  # items: tuples
            out = []  # out: dictionaries

            for item in items:
                out.append(dict(item))

            return out

        else:
            raise Exception("Can't fine the string - \"<script>window.__INITIAL_STATE__=\"")
    else:
        raise Exception("Can't fine the string - \'\"pages\":[\'")


if __name__ == "__main__":
    pages = process_input()
