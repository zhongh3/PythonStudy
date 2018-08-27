import os, subprocess


# original file name:
# e.g. 【不忘初心字幕组】【全场中字】2015.12.06 AKB48剧场Open10周年纪念祭 渡边麻友-8985561_part1.flv
# rename it to "1.flv"
def rename(path):
    files = os.listdir(path)

    for item in files:
        if item.find(".flv") >= 0:
            print(item)
            if len(item.split("part")) > 1:
                new_name = item.split("part")[1]
                print(new_name)
                os.rename(path+item, path+new_name)


# To generate inputs.txt for ffmpeg in the format:
# file '1.flv'
# file '2.flv'
def generate_inputs_txt(path):
    files = os.listdir(path)
    seq = []
    for item in files:
        if item.find(".flv") >= 0:
            seq.append(int(item.split(".flv")[0]))

    # str sort: 1, 10, 2
    # int sort: 1, 2, 10
    seq.sort()

    inputs_txt = open(path+"inputs.txt", "w")
    for item in seq:
        inputs_txt.write("file \'" + str(item) + ".flv\'\n")


def main():
    path = os.getcwd() + "/AKB/"
    rename(path)
    generate_inputs_txt(path)

    os.chdir(path)
    subprocess.call(['ffmpeg', '-f', 'concat', '-i', 'inputs.txt', '-c', 'copy', 'output.mp4'])


if __name__ == "__main__":
    main()
