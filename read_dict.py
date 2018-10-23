file1 = "D:\corpus_clear\dict\dirty.txt"
file2 = "D:\corpus_clear\dict\zh.txt"


with open(file1, 'rb') as f:
    line_ = f.readlines()
    line_1 = [i.decode().split()[0] for i in line_]
    # print(line_1)


with open(file2, 'rb') as f:
    line_ = f.readlines()
    line_2 = [i.decode().split()[0] for i in line_]
    # print(line_2)

dirty_word = set(line_1 + line_2)
